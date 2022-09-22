from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from users.models import CustomUser



class Attendance(models.Model):
    BOOL_CHOICES = ((True, 'Present'), (False, 'Absent'))

    summary = models.TextField(blank=True)
    present = models.BooleanField(choices=BOOL_CHOICES, null=True, default=False, verbose_name="status")
    subject = models.CharField(max_length=140, default='null')
    created = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='students',
    )


    def __str__(self):
        # return self.student.username
        return f"{self.student.first_name} {self.student.last_name}"


    def get_absolute_url(self):
        return reverse('attendance_detail', args=[str(self.id)])
