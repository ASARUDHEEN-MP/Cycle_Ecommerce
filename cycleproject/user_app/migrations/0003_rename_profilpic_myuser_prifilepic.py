# Generated by Django 4.1.5 on 2023-01-27 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_rename_dp_myuser_profilpic_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='profilpic',
            new_name='prifilepic',
        ),
    ]