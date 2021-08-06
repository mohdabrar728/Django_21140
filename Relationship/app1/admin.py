from django.contrib import admin
from .models import Rtable, Stable


# Register your models here.
@admin.register(Rtable)
class ShowR(admin.ModelAdmin):
    list_display = ['name', 'designation', 'age']


@admin.register(Stable)
class ShowR(admin.ModelAdmin):
    list_display = ['shivani']
