# Generated by Django 3.0.4 on 2020-04-17 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage', '0004_auto_20200413_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.FloatField()),
                ('unit_type', models.CharField(max_length=3)),
                ('stock', models.FloatField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Category')),
            ],
        ),
        migrations.CreateModel(
            name='StockOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('quantity_type', models.CharField(max_length=3)),
                ('date', models.DateTimeField(auto_now=True)),
                ('mode', models.CharField(max_length=30)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Product')),
            ],
        ),
        migrations.CreateModel(
            name='StockIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('quantity_type', models.CharField(max_length=3)),
                ('date', models.DateTimeField(auto_now=True)),
                ('mode', models.CharField(max_length=30)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Product')),
            ],
        ),
    ]