# Generated by Django 4.1.4 on 2023-02-06 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0022_products_quantity'),
        ('user_app', '0010_carts_delete_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='carts',
            new_name='cart',
        ),
    ]
