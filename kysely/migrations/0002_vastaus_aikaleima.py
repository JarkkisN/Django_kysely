# Generated by Django 4.1.7 on 2023-04-13 01:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kysely', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vastaus',
            name='aikaleima',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]