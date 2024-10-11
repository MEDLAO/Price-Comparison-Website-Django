from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('PROD_SECRET_KEY')

# Debug settings for production
DEBUG = False

ALLOWED_HOSTS = ['fromsifr.com', 'www.fromsifr.com', 'ec2-35-180-205-132.eu-west-3.compute.amazonaws.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('PROD_DB_NAME'),
        'USER': env('PROD_DB_USER'),
        'PASSWORD': env('PROD_DB_PASSWORD'),
        'HOST': env('PROD_DB_HOST'),
        'PORT': env('PROD_DB_PORT'),
        'OPTIONS': {
            'options': '-c search_path=public',
        },
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'

# AWS SES email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('AWS_SES_EMAIL_HOST')
EMAIL_PORT = env('AWS_SES_PORT')  # TLS port
EMAIL_USE_TLS = True  # use TLS for secure email
EMAIL_HOST_USER = env('AWS_SES_SMTP_USER')
EMAIL_HOST_PASSWORD = env('AWS_SES_SMTP_PASSWORD')
DEFAULT_FROM_EMAIL = 'contact@fromsifr.com'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"redis://:{os.getenv('AWS_REDIS_PASSWORD')}@{os.getenv('AWS_REDIS_ENDPOINT')}/1",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': os.getenv('AWS_REDIS_PASSWORD'),
        },
    }
}
