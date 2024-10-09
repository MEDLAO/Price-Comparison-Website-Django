from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DEV_SECRET_KEY')

# Debug settings for development
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DEV_DB_NAME'),
        'USER': env('DEV_DB_USER'),
        'PASSWORD': env('DEV_DB_PASSWORD'),
        'HOST': env('DEV_DB_HOST'),
        'PORT': env('DEV_DB_PORT'),
        'OPTIONS': {
            'options': '-c search_path=public',
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
