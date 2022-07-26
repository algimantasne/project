# Generated by Django 4.0.6 on 2022-07-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_client_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='Address')),
                ('phone', models.CharField(max_length=12, null=True, verbose_name='Phone')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=12, null=True, verbose_name='Phone'),
        ),
    ]