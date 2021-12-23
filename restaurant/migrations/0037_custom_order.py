# Generated by Django 3.2.9 on 2021-12-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0036_delete_custom_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('num_of_people', models.PositiveIntegerField(blank=True, null=True)),
                ('date_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]