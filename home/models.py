from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_admin=False, is_staff=False, is_superuser=False, is_active=True):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a Password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    image = models.ImageField(upload_to='user', default='')
    password = models.CharField(max_length=90)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_fullname(self):
        return self.first_name + " " + self.last_name


class CompanyInfo(models.Model):
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


class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title


class History(models.Model):
    experience = models.PositiveIntegerField(verbose_name="Experiance Year")
    happy_customer = models.PositiveIntegerField()
    avail_food_item = models.PositiveIntegerField()
    running_order = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'History'

    def __str__(self):
        return str(self.experience)


class Subscription(models.Model):
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


class MealTime(models.Model):
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


class FeatureItems(models.Model):
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
    discount = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.subject}"

