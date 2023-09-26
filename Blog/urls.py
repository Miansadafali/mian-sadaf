from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticlesView.as_view(), name='articles'),
    path('articles/<slug:article_slug>', views.ArticleDetail.as_view(), name='article_detail'),
   
]