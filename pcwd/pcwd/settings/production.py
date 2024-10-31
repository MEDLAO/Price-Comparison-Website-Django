from .base import *
import boto3
from botocore.exceptions import ClientError


def get_ssm_parameter(name, with_decryption=True):
    """Fetch a parameter from AWS SSM Parameter Store."""
    # create a boto3 SSM client using the credentials from the environment variables
    ssm = boto3.client(
        'ssm',
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
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

CSRF_TRUSTED_ORIGINS = ['https://fromsifr.com', 'https://www.fromsifr.com']

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

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
# MEDIA_ROOT = BASE_DIR / 'media'

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
        'LOCATION': f"redis://{get_ssm_parameter('/pcwd/AWS_EC2_PRIVATE_KEY')}:6379/1",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}

# AWS S3 settings for media files
AWS_ACCESS_KEY_ID = get_ssm_parameter('/pcwd/AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_ssm_parameter('/pcwd/AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_ssm_parameter('/pcwd/AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'eu-west-3'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# Media files on S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Static settings
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': get_ssm_parameter('/pcwd/GOOGLE_API_CLIENT_ID'),
            'secret': get_ssm_parameter('/pcwd/GOOGLE_API_SECRET'),
            'key': ''
        }
    }
}
