# Generated by Django 5.0.1 on 2024-02-02 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insulin',
            old_name='author',
            new_name='user',
        ),
    ]
