# Generated by Django 4.1.4 on 2023-02-07 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0015_cartss'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartss',
            name='status',
            field=models.BooleanField(default=False, help_text='0=default,1=Hidden'),
        ),
    ]
