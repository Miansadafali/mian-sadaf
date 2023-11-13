from django.contrib import admin
from .models import Article,  Topic


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'date','get_topics')
    list_filter = ('author', 'date')
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}
    exclude = ['author','summary']
    
    def get_topics(self, obj):
        return ", ".join(topic.name for topic in obj.topics.all())

    get_topics.short_description = 'Topics'
    



class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(Topic, TopicAdmin)
