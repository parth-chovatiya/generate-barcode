# Generated by Django 3.0.6 on 2021-01-10 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210110_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country_id',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer_id',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=5, null=True),
        ),
    ]