from django.db import models

# Create your models here.
class Student(models.Model):
    uid = models.CharField(max_length=70)
    sid = models.CharField(max_length=70, primary_key=True)
    name = models.CharField(max_length=70)
    age = models.CharField(max_length=70)
    cls = models.CharField(max_length=70)

    def __str__(self):
        return str(self.name)