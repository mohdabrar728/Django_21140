from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    msg = models.TextField(max_length=500)

    def __str__(self):
        return (self.name)