# Generated by Django 4.2.3 on 2023-07-23 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_expense_deductible'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='help_text',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
