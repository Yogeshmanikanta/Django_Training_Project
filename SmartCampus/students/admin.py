from django.contrib import admin
from .models import Hall, Booking

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'location')
    search_fields = ('name', 'location')
    list_filter = ('location',)
    ordering = ('name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'hall', 'booked_by', 'start_time', 'end_time')
    list_filter = ('hall', 'start_time')
    search_fields = ('event_name', 'hall__name', 'booked_by__username')
    date_hierarchy = 'start_time'
