# Generated by Django 4.2.1 on 2023-06-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='joke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setup', models.CharField(max_length=200)),
                ('punchline', models.CharField(max_length=400)),
            ],
        ),
    ]
