# Generated by Django 3.0.4 on 2020-04-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.AddField(
            model_name='account',
            name='mobilenumber',
            field=models.CharField(default=9074468705, max_length=60, unique=True),
            preserve_default=False,
        ),
    ]