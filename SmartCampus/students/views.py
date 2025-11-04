from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import View
from django.db import transaction
from django.utils.dateparse import parse_datetime
from django.http import JsonResponse
from .models import Resource
from django.utils.decorators import method_decorator


from .models import (
    Resource,
    LostFound,
    AttendanceRecord,
    Hall,
    Booking,
    CompilerJob,
)

# ----------------------------
# Helper Function
# ----------------------------
def is_student(user):
    return user.role == 'student'


# ----------------------------
# Dashboard
# ----------------------------
@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    """Main student dashboard view."""
    return render(request, 'students/dashboard.html')


# ----------------------------
# Resources
# ----------------------------
@login_required
@user_passes_test(is_student)
def resources(request):
    resources = Resource.objects.all().order_by('-created_at')
    return render(request, 'students/resources.html', {'resources': resources})


# ----------------------------
# Compiler (Online Code Runner)
# ----------------------------
@login_required
@user_passes_test(is_student)
def compiler(request):
    """Compiler page - will integrate API later."""
    return render(request, 'students/compiler.html')


# ----------------------------
# Lost & Found
# ----------------------------
@login_required
@user_passes_test(is_student)
def lost_found(request):
    items = LostFound.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'students/lost_found.html', {'items': items})


# ----------------------------
# Attendance Tracker
# ----------------------------
@login_required
@user_passes_test(is_student)
def attendance(request):
    records = AttendanceRecord.objects.filter(student__user=request.user).order_by('-date')
    return render(request, 'students/attendance.html', {'attendance': records})


# ----------------------------
# Event Scheduler / Hall Booking
# ----------------------------
@login_required
@user_passes_test(is_student)
def events(request):
    events = Booking.objects.filter(approved=True).order_by('start_time')
    halls = Hall.objects.all()
    return render(request, 'students/events.html', {'events': events, 'halls': halls})

@login_required
@user_passes_test(is_student)
def hall_list(request):
    halls = Hall.objects.all()
    return render(request, 'students/hall_list.html', {'halls': halls})
# ----------------------------
# Booking Creation (AJAX)
# ----------------------------
@method_decorator([login_required, user_passes_test(is_student)], name='dispatch') # type: ignore
class BookingCreateView(View):
    def post(self, request):
        hall_id = request.POST.get('hall_id')
        start = parse_datetime(request.POST.get('start'))
        end = parse_datetime(request.POST.get('end'))
        hall = Hall.objects.get(pk=hall_id)

        # Prevent overlap booking
        with transaction.atomic():
            overlapping = Booking.objects.select_for_update().filter(
                hall=hall,
                start_time__lt=end,
                end_time__gt=start
            ).exists()
            if overlapping:
                return JsonResponse(
                    {'ok': False, 'error': 'Hall not available for the selected time'},
                    status=400
                )

            booking = Booking.objects.create(
                hall=hall,
                booked_by=request.user,
                event_name=request.POST.get('event_name', 'Event'),
                start_time=start,
                end_time=end
            )

        return JsonResponse({'ok': True, 'booking_id': booking.pk})
