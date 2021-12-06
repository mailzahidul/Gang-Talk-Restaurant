from django.db import models

# Create your models here.


class Contact_us(models.Model):
    shop_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    about_contact = models.TextField()
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.shop_address


# class ContactMessage(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     subject = models.CharField(max_length=200)
#     phone = models.CharField(max_length=15)
#     message = models.TextField()

#     def __str__(self):
#         return self.name


class LocationDetails(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Shop(models.Model):
    location = models.ForeignKey(LocationDetails, on_delete=models.CASCADE)
    shop = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    district = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=15)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.location.title+"-"+self.shop