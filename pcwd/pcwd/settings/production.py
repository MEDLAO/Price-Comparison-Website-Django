from .base import *
import boto3
from botocore.exceptions import ClientError


def get_ssm_parameter(name, with_decryption=True):
    """Fetch a parameter from AWS SSM Parameter Store."""
    # create a boto3 SSM client using the credentials from the environment variables
    ssm = boto3.client(
        'ssm',
        region_name='eu-west-3',  # Use your specific AWS region
    )

    try:
        parameter = ssm.get_parameter(Name=name, WithDecryption=with_decryption)
        return parameter['Parameter']['Value']
    except ClientError as e:
        print(f"Error fetching {name} from SSM: {e}")
        return None


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_ssm_parameter('/pcwd/PROD_SECRET_KEY')

# Debug settings for production
DEBUG = False

ALLOWED_HOSTS = ['fromsifr.com', 'www.fromsifr.com', 'ec2-35-180-205-132.eu-west-3.compute.amazonaws.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_ssm_parameter('/pcwd/PROD_DB_NAME'),
        'USER': get_ssm_parameter('/pcwd/PROD_DB_USER'),
        'PASSWORD': get_ssm_parameter('/pcwd/PROD_DB_PASSWORD'),
        'HOST': get_ssm_parameter('/pcwd/PROD_DB_HOST'),
        'PORT': get_ssm_parameter('/pcwd/PROD_DB_PORT'),
        'OPTIONS': {
            'options': '-c search_path=public',
        },
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

# AWS SES email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = get_ssm_parameter('/pcwd/AWS_SES_EMAIL_HOST')
EMAIL_PORT = get_ssm_parameter('/pcwd/AWS_SES_PORT')  # TLS port
EMAIL_USE_TLS = True  # use TLS for secure email
EMAIL_HOST_USER = get_ssm_parameter('/pcwd/AWS_SES_SMTP_USER')
EMAIL_HOST_PASSWORD = get_ssm_parameter('/pcwd/AWS_SES_SMTP_PASSWORD')
DEFAULT_FROM_EMAIL = 'contact@fromsifr.com'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"redis://:{get_ssm_parameter('/pcwd/AWS_REDIS_PASSWORD')}@{get_ssm_parameter('/pcwd/AWS_REDIS_ENDPOINT')}/1",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': get_ssm_parameter('/pcwd/AWS_REDIS_PASSWORD'),
        },
    }
}
