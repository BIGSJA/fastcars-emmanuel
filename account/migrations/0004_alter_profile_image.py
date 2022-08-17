# Generated by Django 4.0.6 on 2022-08-17 10:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/static/images/user.jpg', upload_to='profile_images', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg'])]),
        ),
    ]
