# Generated by Django 4.1.4 on 2023-02-16 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0035_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='user',
        ),
        migrations.CreateModel(
            name='Used_Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.coupon')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.myuser')),
            ],
        ),
    ]
