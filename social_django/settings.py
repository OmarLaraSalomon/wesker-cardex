"""
Django settings for social_django project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#^z_7hd(538h=l8luekkv@&12sz#^oq*ferugz4k69u!x%9ti)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['cardex.tescacorporation.com','34.217.74.14' , 'localhost','127.0.0.1',]


#AWS Configuration S3

#[ dafault ] 
#aws_access_key_id  = 'AKIA3YVW5CDSB456QEBF'
#aws_secret_access_key  =  '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'

#s3 = boto3.resource('s3',
#         aws_access_key_id='AKIA3YVW5CDSB456QEBF',
#         aws_secret_access_key='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')

# S3 Bucket Configurations  

AWS_ACCESS_KEY_ID= 'AKIA5E6VJQ4FRDYVXOIH'  

AWS_SECRET_ACCESS_KEY= '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'

AWS_STORAGE_BUCKET_NAME= 'cardexbuckettesca'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION = 'static'

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_REGION_NAME = 'us-west-2' #change to your region

AWS_S3_SIGNATURE_VERSION = 's3v4'

AWS_S3_FILE_OVERWRITE = False  

AWS_DEFAULT_ACL = None  

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'   

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_LOCATION = 'static'
#STATICFILES_STORAGE = 'django_lender.custom_storages.StaticStorage'
STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


MEDIAFILES_LOCATION = 'media'
#DEFAULT_FILE_STORAGE = 'django_lender.custom_storages.MediaStorage'
MEDIA_URL = 'htts://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)



#STATIC_URL = '/static/'

#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')


#Nunca comentar estas dos lineas
LOGIN_REDIRECT_URL = 'inicio'
LOGIN_URL = 'login'



# Application definition

INSTALLED_APPS = [
    'social.apps.SocialConfig',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'rangefilter',
    'django_seed'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'social_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'social_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


#'USER': 'tesca',
#'PASSWORD': 'tesca123',

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cardex',
        'USER': 'postgres',
        'PASSWORD': 'admin123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_REDIRECT_URL = 'inicio'
LOGIN_URL = 'login'
