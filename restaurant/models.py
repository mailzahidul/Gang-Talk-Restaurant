from django.db import models

# Create your models here.


# This Section for Menu

class Meal_category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="meal_category/")
    
    class Meta:
        verbose_name_plural = 'Meal Category'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Custom_order(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    num_of_people = models.PositiveIntegerField(blank=True, null=True)
    date_time = models.DateTimeField()
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    is_response = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Custom Order'

    def __str__(self):
        return self.name


# This Section for Product


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product_tab(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Offer Product Tab'

    def __str__(self):
        return self.name



class Offer(models.Model):
    offer_name = models.CharField(max_length=100)
    product_tab = models.ForeignKey(Product_tab,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.offer_name


class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="product/")
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(Item, blank=True, verbose_name="Items(For Catering & Menu Product)")
    meal_category = models.ForeignKey(Meal_category, on_delete=models.CASCADE, blank=True, null=True)
    is_catering = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    num_of_table = models.PositiveIntegerField()
    num_of_people = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    is_response = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name