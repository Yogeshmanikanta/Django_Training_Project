from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        indexes = [
            models.Index(fields=['code'], name='idx_course_code'),
        ]

    def __str__(self):
        return f"{self.name} ({self.code})"


class Student(models.Model):
    name = models.CharField(max_length=120)
    roll_no = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='students')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['roll_no']
        indexes = [
            models.Index(fields=['roll_no']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return f"{self.roll_no} - {self.name}"


class Attendance(models.Model):
    STATUS_PRESENT = 'P'
    STATUS_ABSENT = 'A'
    STATUS_CHOICES = [
        (STATUS_PRESENT, 'Present'),
        (STATUS_ABSENT, 'Absent'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    marked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'date')
        ordering = ['-date']
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['student', 'date']),
        ]

    def __str__(self):
        return f"{self.student} - {self.date} - {self.get_status_display()}"
    


class Feedback(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Feedback from {self.student.name} ({self.rating}/5)"

