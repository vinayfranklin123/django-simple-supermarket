# Generated by Django 3.0.4 on 2020-04-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_orders_is_delivered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='or_item_name',
            field=models.CharField(max_length=50),
        ),
    ]