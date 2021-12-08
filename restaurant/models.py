from django.db import models

# Create your models here.

class Offer(models.Model):
    offer_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.offer_name


class Food_category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product_for(models.Model):
    prod_for = models.CharField(max_length=100)

    def __str__(self):
        return self.prod_for


class Product_tab(models.Model):
    prod_tab = models.CharField(max_length=100)

    def __str__(self):
        return self.prod_tab


class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="product/")
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    category = models.ManyToManyField(Food_category)
    sku = models.CharField(max_length=50)
    description = models.TextField()
    is_stock = models.BooleanField(default=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    product_for = models.ForeignKey(Product_for, on_delete=models.CASCADE)
    product_tab = models.ForeignKey(Product_tab, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
    


