# Generated by Django 4.1.4 on 2023-02-06 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0012_rename_cart_cartss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartss',
            name='user',
        ),
    ]
