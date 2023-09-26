from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect 
from Blog.models import Articles

# Create your views here.

def Index(request):
    articles = Articles.objects.all().order_by('-Date')[:3]
    return render(request, 'index.html', {
        'articles' : articles
    })

def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')

def Explore(request):
    return render(request, 'explore.html')