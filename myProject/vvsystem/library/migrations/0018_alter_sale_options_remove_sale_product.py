# Generated by Django 4.0.6 on 2022-07-25 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_alter_sale_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={},
        ),
        migrations.RemoveField(
            model_name='sale',
            name='product',
        ),
    ]