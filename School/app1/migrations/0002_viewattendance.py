# Generated by Django 3.2.6 on 2021-08-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attending', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
            ],
        ),
    ]
