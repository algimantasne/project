# Generated by Django 4.0.6 on 2022-07-25 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_alter_sale_options_remove_sale_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['order_No', 'product']},
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.product'),
        ),
    ]
