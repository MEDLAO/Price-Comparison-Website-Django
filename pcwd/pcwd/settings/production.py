from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('PROD_SECRET_KEY')

# Debug settings for production
DEBUG = False

ALLOWED_HOSTS = ['fromsifr.com', 'www.fromsifr.com', 'ec2-35-180-205-132.eu-west-3.compute.amazonaws.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('PROD_DB_NAME'),
        'USER': os.getenv('PROD_DB_USER'),
        'PASSWORD': os.getenv('PROD_DB_PASSWORD'),
        'HOST': os.getenv('PROD_DB_HOST'),
        'PORT': os.getenv('PROD_DB_PORT'),
        'OPTIONS': {
            'options': '-c search_path=public',
        },
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = '/app/media'

# AWS SES email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('AWS_SES_EMAIL_HOST')
EMAIL_PORT = os.getenv('AWS_SES_PORT')  # TLS port
EMAIL_USE_TLS = True  # use TLS for secure email
EMAIL_HOST_USER = os.getenv('AWS_SES_SMTP_USER')
EMAIL_HOST_PASSWORD = os.getenv('AWS_SES_SMTP_PASSWORD')
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
