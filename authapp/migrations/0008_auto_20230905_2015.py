# Generated by Django 3.0.5 on 2023-09-05 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20230905_1149'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Policy',
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
    ]
