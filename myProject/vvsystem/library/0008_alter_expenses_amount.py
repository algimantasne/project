# Generated by Django 4.0.6 on 2022-07-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_expenses_delete_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.CharField(max_length=7, verbose_name='Amount'),
        ),
    ]