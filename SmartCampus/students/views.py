from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_student(user):
    return user.role == 'student'

@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    return render(request, 'students/dashboard.html')
