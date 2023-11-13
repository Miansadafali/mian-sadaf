from django.contrib import admin
from .models import Subscriber
# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    list_filter = ('date',)
    search_fields = ['name', 'email']
    
admin.site.register(Subscriber, SubscriberAdmin)