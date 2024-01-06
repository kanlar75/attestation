# Generated by Django 5.0 on 2024-01-06 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics_network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='electronics_network.company', verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='electronics_network.company', verbose_name='Компания'),
        ),
    ]
