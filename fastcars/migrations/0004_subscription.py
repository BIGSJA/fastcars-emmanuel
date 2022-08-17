# Generated by Django 4.0.6 on 2022-08-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastcars', '0003_alter_testimonial_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('email',),
            },
        ),
    ]