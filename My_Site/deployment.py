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
    'miansadaf.tech',
    'www.miansadaf.tech',
    '127.0.0.1'
]

DEBUG = False

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

 
DATABASES = {
    'default': dj_database_url.config()
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
AWS_S3_REGION_NAME = 'us-east-2'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = 'public-read'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


