# Generated by Django 2.0.1 on 2018-01-27 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkalot', '0004_auto_20180127_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='maps',
            field=models.CharField(default='https://www.google.com/maps/search/?api=1&query=srm+university', max_length=500),
        ),
    ]