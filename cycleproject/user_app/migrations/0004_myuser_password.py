# Generated by Django 4.1.5 on 2023-01-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_rename_profilpic_myuser_prifilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
