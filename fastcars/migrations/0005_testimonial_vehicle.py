# Generated by Django 4.0.6 on 2022-08-10 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0009_remove_brand_brand_logo'),
        ('fastcars', '0004_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.vehicle'),
        ),
    ]
