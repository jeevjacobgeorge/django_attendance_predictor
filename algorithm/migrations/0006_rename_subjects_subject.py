# Generated by Django 4.1 on 2022-08-14 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algorithm', '0005_remove_subjects_day_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subjects',
            new_name='Subject',
        ),
    ]