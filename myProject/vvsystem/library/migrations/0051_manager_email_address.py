# Generated by Django 4.0.6 on 2022-08-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0050_rename_client_sale_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='email_address',
            field=models.CharField(max_length=100, null=True, verbose_name='Email'),
        ),
    ]