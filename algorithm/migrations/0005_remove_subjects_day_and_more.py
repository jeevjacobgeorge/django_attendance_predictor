# Generated by Django 4.1 on 2022-08-11 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithm', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='day',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='number_of_peroids',
        ),
        migrations.AddField(
            model_name='subjects',
            name='number_of_peroids_on_friday',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subjects',
            name='number_of_peroids_on_monday',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subjects',
            name='number_of_peroids_on_thursday',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subjects',
            name='number_of_peroids_on_tuesday',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subjects',
            name='number_of_peroids_on_wednesday',
            field=models.IntegerField(default=0),
        ),
    ]