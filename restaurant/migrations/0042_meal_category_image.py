# Generated by Django 3.2.9 on 2021-12-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0041_menu_package_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal_category',
            name='image',
            field=models.ImageField(default=1, upload_to='meal_category/'),
            preserve_default=False,
        ),
    ]
