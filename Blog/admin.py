from django.contrib import admin
from .models import Article,  Topic


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'date')
    list_filter = ('author', 'date')
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}
    exclude = ['author',]
    
    
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(Topic, TopicAdmin)
