# Generated by Django 4.1.4 on 2023-01-31 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0011_alter_categorys_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]