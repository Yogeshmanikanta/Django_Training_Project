from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


# 1️⃣ Resources
class Resource(models.Model):
    UPLOAD_TYPES = [
        ('pdf', 'PDF'),
        ('ppt', 'PPT'),
        ('doc', 'DOC'),
        ('zip', 'ZIP'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='resources/%Y/%m/%d/')
    uploaded_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='resources'
    )
    course = models.ForeignKey(
        'faculty.Course', on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['created_at'])]

    def __str__(self):
        return self.title


# 2️⃣ Lost & Found
class LostFound(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('claimed', 'Claimed'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='lost')
    location = models.CharField(max_length=200, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['status', 'created_at'])]

    def __str__(self):
        return f"{self.title} ({self.status})"


# 3️⃣ Attendance
class ClassRoom(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(
        'faculty.Course', on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AttendanceRecord(models.Model):
    student = models.ForeignKey(
        'faculty.Student', on_delete=models.CASCADE, related_name='attendance_records'
    )
    classroom = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE, related_name='attendances'
    )
    date = models.DateField()
    status = models.CharField(
        max_length=1, choices=[('P', 'Present'), ('A', 'Absent')]
    )
    marked_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='marked_attendances'
    )
    marked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'classroom', 'date')
        indexes = [models.Index(fields=['classroom', 'date'])]

    def __str__(self):
        return f"{self.student} - {self.date} ({self.status})"


# 4️⃣ Event Scheduler / Hall Booking
class Hall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='hall_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.event_name} - {self.hall.name}"


# 5️⃣ Compiler Job (Execution Log)
class CompilerJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    language = models.CharField(max_length=50)
    source = models.TextField()
    stdin = models.TextField(blank=True)
    result = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    external_id = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"{self.user} - {self.language} ({self.status})"
