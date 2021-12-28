# Generated by Django 3.2.9 on 2021-12-26 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
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
                ('is_response', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Custom Order',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Meal_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='meal_category/')),
            ],
            options={
                'verbose_name_plural': 'Meal Category',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Offer Product Tab',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('num_of_table', models.PositiveIntegerField()),
                ('num_of_people', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('is_response', models.BooleanField(default=False)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='product/')),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('in_stock', models.BooleanField(default=True)),
                ('is_catering', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(to='restaurant.Category')),
                ('items', models.ManyToManyField(blank=True, to='restaurant.Item', verbose_name='Items(For Catering & Menu Product)')),
                ('meal_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.meal_category')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.offer')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='product_tab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.product_tab'),
        ),
    ]
