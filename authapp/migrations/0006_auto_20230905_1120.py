# Generated by Django 3.0.5 on 2023-09-05 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20230904_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='FullName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='price',
        ),
    ]
