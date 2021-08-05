from django.db import models

# Create your models here.
class ModForms(models.Model):
    name = models.CharField(label='Your Name', label_suffix=':', initial='mr/mrs', max_length=30)
    email = models.EmailField(max_length=30)
    passwd = models.CharField(max_length=10)
    id = models.IntegerField()
    subject = models.CharField(max_length=100, help_text='100 characters max.')
    url = models.URLField(initial='http://')
    contact = models.IntegerField()
    sname = models.CharField()
    message = models.CharField()
    time = models.DateTimeField()
    checkbox = models.BooleanField()
    null = models.NullBooleanField()