from django.db import models

# Create your models here.
class User(models.Model):
 email = models.EmailField(max_length=100)
 subject = models.TextField(max_length=100)
 mail = models.TextField(max_length=250)