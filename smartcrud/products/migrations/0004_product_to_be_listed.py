# Generated by Django 4.1.1 on 2022-09-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='to_be_listed',
            field=models.BooleanField(default=True),
        ),
    ]