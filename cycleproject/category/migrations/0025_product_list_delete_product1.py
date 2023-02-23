# Generated by Django 4.1.4 on 2023-02-08 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0024_product1'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('image1', models.ImageField(upload_to='products')),
                ('image2', models.ImageField(upload_to='products')),
                ('image3', models.ImageField(upload_to='products')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=6, max_digits=10)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.CharField(default='SOME STRING', max_length=140)),
                ('status', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('quantity', models.IntegerField(default=0)),
                ('category', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.categorys')),
            ],
        ),
        migrations.DeleteModel(
            name='product1',
        ),
    ]
