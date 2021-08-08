# Generated by Django 3.2.5 on 2021-08-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='mail',
            field=models.TextField(default='test', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='subject',
            field=models.TextField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
