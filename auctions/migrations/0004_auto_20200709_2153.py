# Generated by Django 3.0.8 on 2020-07-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200709_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='current_bid',
            field=models.IntegerField(blank=True, default=models.IntegerField()),
        ),
    ]