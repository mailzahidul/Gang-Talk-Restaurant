# Generated by Django 3.2.9 on 2021-12-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211219_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visit_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]