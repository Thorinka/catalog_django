# Generated by Django 4.2.3 on 2023-08-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_key',
            field=models.IntegerField(blank=True, max_length=12, null=True, verbose_name='ключ'),
        ),
    ]
