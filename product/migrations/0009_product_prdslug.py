# Generated by Django 4.0.4 on 2022-06-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_prdimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDSLug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
