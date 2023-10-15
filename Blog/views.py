
from typing import Any, Dict
from .models import Articles, Topics
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render


class ArticlesView(ListView):
    model = Articles
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self.request.GET.get('topic')
        
        if topic:
            context['articles'] = Articles.objects.filter(Topic__Slug=topic).order_by('?')
        else:
            context['articles'] = Articles.objects.order_by('?')

        context['latest'] = Articles.objects.latest('Date')
        context['topics'] = Topics.objects.all()
        return context

    
class ArticleDetail(DetailView):
    model = Articles
    template_name = 'article_detail.html'
    slug_field = 'Slug'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.Tags.all()
        return context

    
