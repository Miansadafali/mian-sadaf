from django.db import models
from django.urls import reverse

# Create your models here.

class Articles(models.Model):
    Title = models.CharField(max_length=100)
    Slug = models.SlugField(unique=True)
    Author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Body = models.TextField()
    Summary = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField(upload_to='images/', default='images/Account_dp.png')
    Category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True)
    Tags = models.ManyToManyField('Tag', blank=True)
    Topic = models.ManyToManyField('Topics', blank=True)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"article_slug": self.Slug})
    



class Category(models.Model):
    Name = models.CharField(max_length=100)
    Slug = models.SlugField(unique=True)

    def __str__(self):
        return self.Name


class Tag(models.Model):
    Name = models.CharField(max_length=100)
    Slug = models.SlugField(unique=True)

    def __str__(self):
        return self.Name
    
class Topics(models.Model):
    Name = models.CharField(max_length=100)
    Slug = models.SlugField(unique=True)

    def __str__(self):
        return self.Name

