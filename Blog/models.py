from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    body = FroalaField()
    summary = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, default='images/default.jpg')
    topics = models.ManyToManyField('Topic', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"article_slug": self.slug})
    

class Topic(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

