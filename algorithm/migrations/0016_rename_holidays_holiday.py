# Generated by Django 4.1 on 2022-10-09 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algorithm', '0015_holidays_remove_subject_subject_branch_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='holidays',
            new_name='holiday',
        ),
    ]
