# Generated by Django 4.0.4 on 2022-05-08 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
