# Generated by Django 3.2.5 on 2021-07-27 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LM_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
            ],
        ),
    ]
