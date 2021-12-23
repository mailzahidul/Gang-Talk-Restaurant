# Generated by Django 3.2.9 on 2021-12-21 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0048_delete_catering_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product_tab',
            options={'verbose_name_plural': 'Offer Product Tab'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='assign_tab',
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_catering',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meal_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.meal_category'),
        ),
        migrations.DeleteModel(
            name='Catering_tab',
        ),
    ]
