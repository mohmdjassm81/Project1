# Generated by Django 4.0.4 on 2022-06-10 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_commandspost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commandspost',
            name='PRDIPriority',
        ),
    ]
