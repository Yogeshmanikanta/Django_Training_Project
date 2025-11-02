from django.contrib import admin
from .models import Course, Student, Attendance,Feedback


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    ordering = ('name',)
    list_filter = ('code',)
    list_per_page = 20


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'email', 'course', 'joined_at')
    search_fields = ('name', 'roll_no', 'email')
    list_filter = ('course',)
    ordering = ('roll_no',)
    list_per_page = 25


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status', 'marked_at')
    list_filter = ('status', 'date')
    search_fields = ('student__name', 'student__roll_no')
    ordering = ('-date',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('student__name',)
    ordering = ('-created_at',)