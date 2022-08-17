# Generated by Django 4.0.6 on 2022-08-03 03:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_logo', models.ImageField(upload_to='brand_images', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('brand_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
