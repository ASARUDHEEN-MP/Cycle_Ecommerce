# Generated by Django 4.1.5 on 2023-01-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0014_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='categorys',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]