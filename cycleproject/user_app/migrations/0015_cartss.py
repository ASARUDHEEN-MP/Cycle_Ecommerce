# Generated by Django 4.1.4 on 2023-02-06 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0022_products_quantity'),
        ('user_app', '0014_delete_cartss'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_qty', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.myuser')),
            ],
        ),
    ]