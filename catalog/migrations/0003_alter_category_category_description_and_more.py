# Generated by Django 4.2.3 on 2023-07-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_changed_date_product_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(),
        ),
    ]