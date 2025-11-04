from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student_dashboard'),

    # Resources
    path('resources/', views.resources, name='resources'),

    # Compiler
    path('compiler/', views.compiler, name='compiler'),

    # Lost & Found
    path('lost_found/', views.lost_found, name='lost_found'),

    # Attendance
    path('attendance/', views.attendance, name='attendance'),

    # Events and Halls
    path('events/', views.events, name='events'),
    path('booking/create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('halls/', views.hall_list, name='hall_list'),

]
