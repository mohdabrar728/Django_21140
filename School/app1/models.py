from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)


class ViewAttendance(models.Model):
    student_id = models.IntegerField(primary_key=True)
    date  = models.DateField()
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    attending = models.BooleanField(choices=BOOL_CHOICES)

    def __str__(self):
        return date