import os
from .settings import *

SECRET_KEY = os.environ('SECRET_KEY')

ALLOWED_HOSTS = [os.environ('ALLOWED_HOSTS')] 

DEBUG = os.environ('DEBUG', True)

MIDDLEWARE = [
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

connection_string = os.environ('DATABASE_URL')
parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split(';')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parameters['dbname'],
        'HOST': parameters['host'],
        'USER': parameters['username'],
        'PASSWORD': parameters['password'],
    }
}

