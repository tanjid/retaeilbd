# Generated by Django 4.1 on 2022-08-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock_qty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]