from django.db import models

# Create your models here.
class LM_Model(models.Model):
    book_name =  models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

