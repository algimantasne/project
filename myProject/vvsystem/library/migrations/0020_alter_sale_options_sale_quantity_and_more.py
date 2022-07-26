# Generated by Django 4.0.6 on 2022-07-25 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_alter_sale_options_sale_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['order_No']},
        ),
        migrations.AddField(
            model_name='sale',
            name='quantity',
            field=models.CharField(max_length=5, null=True, verbose_name='Quantity, pcs'),
        ),
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(help_text='Product information', max_length=1000, verbose_name='Summary'),
        ),
    ]
