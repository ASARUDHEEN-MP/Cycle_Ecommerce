# Generated by Django 4.1.4 on 2023-02-14 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0033_orderitem_delete_orderitems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order',
            new_name='orderit',
        ),
    ]
