# Generated by Django 3.0.5 on 2023-09-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_booking_policy_rental'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Duedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rental',
            name='Duedate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
