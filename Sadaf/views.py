from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect 
from Blog.models import Article
from .form import SubscriberForm

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def Index(request):
    articles = Article.objects.all().order_by('-date')[:3]
    return render(request, 'index.html', {
        'Articles' : articles
    })

def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')

def Explore(request):
    return render(request, 'explore.html')



@csrf_exempt  # For simplicity in this example; consider adding proper CSRF protection
def Subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
            return JsonResponse({'success': True, 'message': 'Subscription successful!'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid email'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
