# Generated by Django 4.2.3 on 2023-07-22 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'публикация', 'verbose_name_plural': 'публикации'},
        ),
    ]
