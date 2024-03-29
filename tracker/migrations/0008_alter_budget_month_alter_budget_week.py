# Generated by Django 4.2.3 on 2023-07-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_alter_budget_annual_alter_budget_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='month',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='budget',
            name='week',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
