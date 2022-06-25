# Generated by Django 4.0.4 on 2022-05-26 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(max_length=100)),
                ('PRDDesc', models.TextField(max_length=500)),
                ('PRDPrice', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PRDCost', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PRDCreated', models.DateTimeField()),
            ],
        ),
    ]
