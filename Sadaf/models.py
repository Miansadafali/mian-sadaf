from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    


