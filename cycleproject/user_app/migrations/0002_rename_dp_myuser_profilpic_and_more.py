# Generated by Django 4.1.5 on 2023-01-27 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='DP',
            new_name='profilpic',
        ),
        migrations.RenameField(
            model_name='myuser',
            old_name='first_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='last_name',
        ),
    ]