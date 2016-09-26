"""
Django settings for Andromeda project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.six.moves import configparser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

with open("etc/key.txt", "r") as f:
    SECRET_KEY = f.read().strip()

ALLOWED_HOSTS = ['*']

APPEND_SLASH = False


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'registry',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'registry.middleware.ExceptionsHandleMiddleware',
    'registry.middleware.CustomHeaderMiddleware',
)

SECURE_CONTENT_TYPE_NOSNIFF = True

ROOT_URLCONF = 'andromeda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'andromeda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 15,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'registry.renderers.ManifestV1Renderer',
        'registry.renderers.ManifestV2Renderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'registry.parsers.ManifestV2Parser',
        'registry.parsers.ManifestV1Parser',
    )
}

# Registry Configurations

CUSTOM_HEADERS = {
    "Docker-Distribution-Api-Version": "registry/2.0",
    "X-Content-Type-Options": "nosniff",
}

config = configparser.ConfigParser()
config.read("etc/andromeda.ini")

REPO_DIR = config['storage']['repo_dir']

BLOB_DIR = config['storage']['blob_dir']
