# Generated by Django 3.2.9 on 2021-12-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20211208_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]