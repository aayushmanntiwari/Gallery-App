# Generated by Django 3.2.3 on 2021-05-26 16:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
