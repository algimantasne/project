# Generated by Django 4.0.6 on 2022-07-21 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_sale_alter_client_first_name_alter_client_last_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Product',
        ),
    ]