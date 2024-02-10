# Generated by Django 5.0.1 on 2024-02-09 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0012_alter_cgm_sensor_life'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cgm',
            old_name='sensor_life',
            new_name='sensor_life_in_days',
        ),
        migrations.RemoveField(
            model_name='cgm',
            name='time_changed',
        ),
        migrations.RemoveField(
            model_name='glucose',
            name='time_taken',
        ),
        migrations.RemoveField(
            model_name='insulin',
            name='time_administered',
        ),
        migrations.RemoveField(
            model_name='insulinchanged',
            name='time_changed',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='time',
        ),
    ]