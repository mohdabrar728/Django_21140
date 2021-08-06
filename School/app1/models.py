from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)


class ViewAttendance(models.Model):
    username = models.CharField(max_length=70)
    date_of_attend = models.DateField(max_length=70)
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    attending = models.BooleanField(choices=BOOL_CHOICES)


class ApplyForLeave(models.Model):
    username = models.CharField(max_length=70)
    date_of_leave = models.DateField(max_length=70)
    CHOICES = (
        ('C', 'Casual Leave'), ('L', 'Loss of Pay'), ('S', 'Sick Leave'),
    )
    type_of_leave = models.CharField(max_length=70, choices=CHOICES)
    message = models.CharField(max_length=70)


class Feedback(models.Model):
    subject = models.CharField(max_length=70)
    message = models.CharField(max_length=200)
