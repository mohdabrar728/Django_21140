from django.contrib import admin
from .models import LM_Model


# Register your models here.
@admin.register(LM_Model)
class Admin_LM_Model(admin.ModelAdmin):
    list_display = ['id','book_name', 'author_name', 'category', 'ISBN', 'quantity']
