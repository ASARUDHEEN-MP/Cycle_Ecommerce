# Generated by Django 4.1.5 on 2023-01-31 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0013_product_delete_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products'),
        ),
    ]
