# Generated by Django 4.0.6 on 2022-08-01 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0041_remove_client_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expenses',
            new_name='Expense',
        ),
    ]