# Generated by Django 4.1.4 on 2023-02-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0037_alter_used_coupon_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
    ]