# Generated by Django 4.2.9 on 2024-01-30 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
