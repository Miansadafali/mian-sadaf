from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('explore/', views.Explore, name='explore'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('subscribe/', views.Subscribe, name='subscribe'),

    
]