# Generated by Django 4.1.4 on 2023-02-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_myuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='status',
            field=models.BooleanField(default=False, help_text='0=default,1=Hidden'),
        ),
    ]
