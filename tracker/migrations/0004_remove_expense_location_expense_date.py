# Generated by Django 4.2.3 on 2023-07-23 23:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_expense_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='location',
        ),
        migrations.AddField(
            model_name='expense',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
