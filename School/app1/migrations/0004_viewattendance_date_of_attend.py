# Generated by Django 3.2.5 on 2021-08-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210803_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewattendance',
            name='date_of_attend',
            field=models.DateField(default=None, max_length=70),
            preserve_default=False,
        ),
    ]
