# Generated by Django 3.2.9 on 2021-12-20 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0040_auto_20211220_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_package',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
