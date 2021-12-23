# Generated by Django 3.2.9 on 2021-12-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20211220_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_us',
            options={'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='feature_items',
            options={'verbose_name_plural': 'Feature Items'},
        ),
        migrations.AlterModelOptions(
            name='gang_talk',
            options={'verbose_name_plural': 'Gang Talks'},
        ),
        migrations.AlterModelOptions(
            name='meal_time',
            options={'verbose_name_plural': 'Meal Time'},
        ),
        migrations.AddField(
            model_name='company_info',
            name='tag_line',
            field=models.CharField(default='An Ideal Restaurant', max_length=100),
            preserve_default=False,
        ),
    ]
