from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Designation(models.Model):
    designation = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Author Status"
    
    def __str__(self):
        return self.designation

class Status(models.Model):
    status = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.status

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

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    photo = models.ImageField(upload_to="user/", blank=True, null=True)
    author_status = models.ForeignKey(Designation, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/post/feature_img/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default='pending')
    is_featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    visit_count = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        

class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name='reply')
    name = models.CharField(max_length=200, null=True, blank=False)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" { self.name } |{ self.created_at }"
