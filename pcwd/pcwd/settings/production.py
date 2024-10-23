from .base import *
from .utils import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_or_ssm('PROD_SECRET_KEY', '/pcwd/PROD_SECRET_KEY')

# Debug settings for production
DEBUG = False

ALLOWED_HOSTS = ['fromsifr.com', 'www.fromsifr.com', 'ec2-35-180-205-132.eu-west-3.compute.amazonaws.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_or_ssm('PROD_DB_NAME', '/pcwd/PROD_DB_NAME'),
        'USER': get_env_or_ssm('PROD_DB_USER', '/pcwd/PROD_DB_USER'),
        'PASSWORD': get_env_or_ssm('PROD_DB_PASSWORD', '/pcwd/PROD_DB_PASSWORD'),
        'HOST': get_env_or_ssm('PROD_DB_HOST', '/pcwd/PROD_DB_HOST'),
        'PORT': get_env_or_ssm('PROD_DB_PORT', '/pcwd/PROD_DB_PORT'),
        'OPTIONS': {
            'options': '-c search_path=public',
        },
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

# AWS SES email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = get_env_or_ssm('AWS_SES_EMAIL_HOST', '/pcwd/AWS_SES_EMAIL_HOST')
EMAIL_PORT = get_env_or_ssm('AWS_SES_PORT', '/pcwd/AWS_SES_PORT')  # TLS port
EMAIL_USE_TLS = True  # use TLS for secure email
EMAIL_HOST_USER = get_env_or_ssm('AWS_SES_SMTP_USER', '/pcwd/AWS_SES_SMTP_USER')
EMAIL_HOST_PASSWORD = get_env_or_ssm('AWS_SES_SMTP_PASSWORD', '/pcwd/AWS_SES_SMTP_PASSWORD')
DEFAULT_FROM_EMAIL = 'contact@fromsifr.com'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"redis://:{get_env_or_ssm('AWS_REDIS_PASSWORD', '/pcwd/AWS_REDIS_PASSWORD')}@{get_env_or_ssm('AWS_REDIS_ENDPOINT', '/pcwd/AWS_REDIS_ENDPOINT')}/1",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': get_env_or_ssm('AWS_REDIS_PASSWORD', '/pcwd/AWS_REDIS_PASSWORD'),
        },
    }
}
