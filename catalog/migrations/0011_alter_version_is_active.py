# Generated by Django 4.2.3 on 2023-08-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]
