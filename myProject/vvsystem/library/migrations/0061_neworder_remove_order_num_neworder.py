# Generated by Django 4.0.6 on 2022-08-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0060_order_num_neworder'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newOrder_No', models.CharField(max_length=200, null=True, verbose_name='newOrder_No')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='num_newOrder',
        ),
    ]