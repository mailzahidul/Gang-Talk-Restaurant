from django.db import models
from restaurant.models import Meal_category, Category

# Create your models here.


class Company_info(models.Model):
    title = models.CharField(max_length=120)
    name = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=100)
    fav_icon = models.ImageField(upload_to="company_info/")
    logo = models.ImageField(upload_to="company_info/")
    footer_logo = models.ImageField(upload_to="company_info/")
    shop_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    about = models.TextField()
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Company Information'


    def __str__(self):
        return self.shop_address

class Shop(models.Model):
    shop_title = models.CharField(max_length=50)    
    address = models.CharField(max_length=150)
    district = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=15)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.shop_title


class About_us(models.Model):
    author_title= models.CharField(max_length=150)
    author_des=models.TextField()

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.author_title


class History(models.Model):
    experience=models.PositiveIntegerField()
    happy_customer=models.PositiveIntegerField()
    avail_food_item=models.PositiveIntegerField()
    running_order=models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'History'

    def __str__(self):
        return str(self.experience)


class Subscribtion(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='chef_photo/')

    def __str__(self):
        return self.name


# Home page Models...

class Gang_talk(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Gang Talks Home Content'

    def __str__(self):
        return self.title


class Meal_time(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=200)
    image = models.ImageField(upload_to='meal_time/')

    class Meta:
        verbose_name_plural = 'Meal Time'

    def __str__(self):
        return self.name


class Feature(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


class Feature_items(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to="features/")
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Feature Items'
    
    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="slider/")
    discount_percent = models.PositiveIntegerField()

    def __str__(self):
        return self.title

