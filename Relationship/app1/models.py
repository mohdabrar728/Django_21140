from django.db import models


# Create your models here.
class Rtable(models.Model):
    name = models.CharField(max_length=70)
    designation = models.CharField(max_length=70)
    age = models.IntegerField()


class Stable(models.Model):
    shivani = models.OneToOneField(
        Rtable,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    test = models.CharField(max_length=54)
