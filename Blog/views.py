
from typing import Any, Dict
from .models import Article, Topic
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render


class ArticleView(ListView):
    model = Article
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self.request.GET.get('topic')
        
        if topic:
            context['articles'] = Article.objects.filter(topics__slug=topic).order_by('?')
        else:
            context['articles'] = Article.objects.order_by('?')

        # context['latest'] = Article.objects.latest('date')
        context['topics'] = Topic.objects.all()
        return context

    
class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        context['recent_posts'] = Article.objects.order_by('-date').exclude(slug=self.object.slug).all()[:3]
        return context

    
