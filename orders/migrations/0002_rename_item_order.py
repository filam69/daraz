# Generated by Django 5.0.7 on 2024-07-11 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Order',
        ),
    ]
