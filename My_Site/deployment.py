import os

from django.http import HttpResponsePermanentRedirect
from .settings import *
import dj_database_url


class WWWRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if not host.startswith('www.'):
            new_url = '{}://www.{}{}'.format(
                'https' if request.is_secure() else 'http',
                host,
                request.path
            )
            return HttpResponsePermanentRedirect(new_url)
        return self.get_response(request)
    

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    'mian-sadaf-093df2897493.herokuapp.com',
    'www.miansadaf.tech'
]

DEBUG = False

MIDDLEWARE = [
    'My_Site.deployment.WWWRedirectMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
 
DATABASES = {
    'default': dj_database_url.config()
}

