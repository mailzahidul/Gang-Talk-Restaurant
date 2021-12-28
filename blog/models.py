from django.db import models
from home.models import User

# Create your models here.

STATUS = (
       ('published', 'Published'),
       ('pending', 'Pending')
)


AUTHOR = (
       ('admin', 'Admin'),
       ('editor', 'Editor'),
       ('moderator', 'Moderator'),
)

class Categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/post/feature_img/')
    gallery_1 = models.ImageField(upload_to='blog/post/feature_img/', blank=True, null=True)
    gallery_2 = models.ImageField(upload_to='blog/post/feature_img/', blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    is_featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    created_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title