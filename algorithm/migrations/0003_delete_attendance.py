# Generated by Django 4.1 on 2022-08-11 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algorithm', '0002_alter_attendance_day'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]