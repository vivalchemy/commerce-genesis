# Generated by Django 5.1.5 on 2025-01-29 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
