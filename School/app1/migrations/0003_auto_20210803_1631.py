# Generated by Django 3.2.6 on 2021-08-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_viewattendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewattendance',
            name='id',
        ),
        migrations.AddField(
            model_name='viewattendance',
            name='student_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
