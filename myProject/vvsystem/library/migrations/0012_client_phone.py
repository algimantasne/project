# Generated by Django 4.0.6 on 2022-07-21 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_client_address_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=11, null=True, verbose_name='Phone'),
        ),
    ]
