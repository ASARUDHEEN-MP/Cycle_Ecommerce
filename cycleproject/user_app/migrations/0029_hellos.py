# Generated by Django 4.1.5 on 2023-02-13 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0028_alter_order_payment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='hellos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namess', models.CharField(max_length=15, null=True)),
                ('name', models.TextField(max_length=15, null=True)),
            ],
        ),
    ]