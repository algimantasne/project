# Generated by Django 4.0.6 on 2022-07-31 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0040_client_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='description',
        ),
    ]
