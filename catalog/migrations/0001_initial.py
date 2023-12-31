# Generated by Django 4.2.3 on 2023-07-15 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, verbose_name='категория')),
                ('category_description', models.TextField(verbose_name={'blank': True, 'null': True})),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, verbose_name='наименование')),
                ('product_price', models.IntegerField(max_length=10, verbose_name='цена')),
                ('product_description', models.TextField(verbose_name={'blank': True, 'null': True})),
                ('product_image', models.ImageField(upload_to='products/', verbose_name={'blank': True, 'null': True})),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='продукт', to='catalog.category')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
