# Generated by Django 5.0.1 on 2024-01-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics_network', '0002_alter_contact_company_alter_product_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Компания'),
        ),
    ]