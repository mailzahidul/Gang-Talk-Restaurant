# Generated by Django 3.2.9 on 2021-12-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0037_custom_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_order',
            name='is_response',
            field=models.BooleanField(default=False),
        ),
    ]
