# Generated by Django 4.2.1 on 2023-06-10 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0002_joke_date_submitted_joke_verified_alter_joke_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joke',
            old_name='setup',
            new_name='name',
        ),
    ]
