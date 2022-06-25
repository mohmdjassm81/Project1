# Generated by Django 4.0.4 on 2022-06-10 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_delete_commandspost'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandsPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIName', models.CharField(max_length=600)),
                ('PRDICommands', models.TextField(max_length=600)),
                ('PRDItitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='التعليقات على المنتج')),
            ],
        ),
    ]
