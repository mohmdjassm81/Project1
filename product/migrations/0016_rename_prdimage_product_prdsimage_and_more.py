# Generated by Django 4.0.4 on 2022-06-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_product_prdimage1_product_prdimage2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='PRDImage',
            new_name='PRDSImage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='PRDImage1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='PRDImage2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='PRDImage3',
        ),
        migrations.AddField(
            model_name='product',
            name='PRDSImage1',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='1صور صغيرة للمنتج'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDSImage2',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='2صور صغيرة للمنتج'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDSImage3',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='3صور صغيرة للمنتج'),
        ),
    ]