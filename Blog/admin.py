from django.contrib import admin
from .models import Articles, Category, Tag, Topics

class BlogAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Author', 'Date')
    list_filter = ('Author', 'Date')
    search_fields = ('Title', 'Body')
    prepopulated_fields = {'Slug': ('Title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ('Name',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ('Name',)}

class TopicsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ('Name',)}

admin.site.register(Articles, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Topics, TopicsAdmin)

# Register your models here.
