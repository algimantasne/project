# Generated by Django 4.0.6 on 2022-07-28 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0032_alter_productinstance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
