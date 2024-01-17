from django.urls import include, path
from . import views

urlpatterns = [
    path('articles/', views.ArticleView.as_view(), name='articles'),
    path('articles/topic/<slug:topic>', views.ArticleView.as_view(), name='articles_by_topic'),
    path('articles/<slug:article_slug>', views.ArticleDetail.as_view(), name='article_detail'),
   path('froala_editor/', include('froala_editor.urls')),
]