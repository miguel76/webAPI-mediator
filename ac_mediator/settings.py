"""
Django settings for ac_mediator project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url
import raven


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default_secret_key')

# Debug, allowed hosts and database
if os.getenv('DEPLOY_ENV', 'dev') == 'prod':
    if SECRET_KEY == 'default_secret_key':
        print("Please configure your secret key by setting DJANGO_SECRET_KEY environment variable")
    DEBUG = False
    ALLOWED_HOSTS = ['localhost', 'asplab-web1', 'm.audiocommons.org', 'asplab-web1.s.upf.edu', 'docker.sb.upf.edu']
else:
    DEBUG = True
DATABASE_URL_ENV_NAME = 'DJANGO_DATABASE_URL'
DATABASES = {'default': dj_database_url.config(
    DATABASE_URL_ENV_NAME, default='postgres://postgres:postgres@db/ac_mediator')}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'accounts',
    'api',
    'rest_framework',
    'oauth2_provider',
    'developers',
    'services',
    'docs',
    'raven.contrib.django.raven_compat',
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

ROOT_URLCONF = 'ac_mediator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ac_mediator.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = '/static/'


# API settings
ALLOW_UNAUTHENTICATED_API_REQUESTS_ON_DEBUG = True
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated' if not DEBUG or not ALLOW_UNAUTHENTICATED_API_REQUESTS_ON_DEBUG
        else 'rest_framework.permissions.AllowAny',
    ),
    'EXCEPTION_HANDLER': 'api.utils.custom_exception_handler',
    'URL_FORMAT_OVERRIDE': None,  # disable DRF use of 'format' parameter (we have our own)
}
OAUTH2_PROVIDER_APPLICATION_MODEL = 'api.ApiClient'
OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS': 60*60*24,  # 1 day
    'REFRESH_TOKEN_EXPIRE_SECONDS': 60*60*15,  # 2 weeks
    'AUTHORIZATION_CODE_EXPIRE_SECONDS': 10*60,  # 10 minutes
    'SCOPES': {'read': 'Read scope'},
    'OAUTH2_VALIDATOR_CLASS': 'api.utils.ACOAuth2Validator',
}

JSON_LD_FORMAT_KEY = 'jsonld'
JSON_FORMAT_KEY = 'json'
DEFAULT_RESPONSE_FORMAT = JSON_FORMAT_KEY

# Registration
AUTH_USER_MODEL = 'accounts.Account'
LOGIN_URL = '/login/'
LOGOUT_URL = '/'
LOGIN_REDIRECT_URL = '/'

# Site
BASE_URL = os.getenv('DJANGO_BASE_URL', 'http://example.com')

# Documentation
DOCS_ROOT = os.path.join(BASE_DIR, 'docs/_build/html')
DOCS_ACCESS = 'public'

# Redis
REDIS_HOST = 'redis'  # Host where redis is running (we use docker alias here)
REDIS_PORT = 6379

# Celery
CELERY_BROKER_URL = "redis://redis"
CELERY_RESULT_BACKEND = "redis://redis"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Europe/Madrid'

# Set this to False so that requests are submitted sequentially and from the webserver when in DEBUG mode instead of
# in parallel and using Celery. This can be useful so that Celery workers don't need to be restarted when making
# changes to the code
USE_CELERY_IN_DEBUG_MODE = False

# Shared respones backend and async responses
DELETE_RESPONSES_AFTER_CONSUMED = False
RESPONSE_EXPIRY_TIME = 3600*24  # Response objects are deleted after 24 hours

RAVEN_CONFIG = {
    'dsn': os.getenv('SENTRY_DSN', None),
}

# Email configuration
DEFAULT_FROM_EMAIL = 'Audio Commons <audiocommons@upf.edu>'
EMAIL_SUBJECT_PREFIX = '[AudioCommons] '
EMAIL_HOST = 'smtp-rec.upf.edu'
EMAIL_PORT = 25

if DEBUG:
    # In development environment, use email file backend
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, "mail")

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'simplest': {
            'format': '%(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'stdout': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'gelf': {
            'class': 'logging.NullHandler',  # This will be redefined later if configuration is provided
        },
    },
    'loggers': {
        'management': {
            'handlers': ['stdout', 'gelf'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

if DEBUG:
    # In development we log all requests made into a file
    LOGS_BASE_DIR = os.path.join(BASE_DIR, 'logs')
    if not os.path.exists(LOGS_BASE_DIR):
        os.makedirs(LOGS_BASE_DIR)
    LOGGING['handlers'].update({
        'logfile_requests': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_BASE_DIR, 'requests.log'),
            'formatter': 'simplest'
        }
    })
    LOGGING['loggers'].update({
        'requests_sent': {
            'handlers': ['logfile_requests'],
            'level': 'INFO',
            'propagate': False,
        }
    })


# Read logserver config settings, if present, then update the corresponding handler
GELF_IP_ADDRESS = os.getenv('GELF_IP_ADDRESS', None)
GELF_PORT = int(os.getenv('GELF_PORT', 0))
if GELF_IP_ADDRESS is not None and GELF_PORT is not None:
    LOGGING['handlers'].update(
        {
            'gelf': {
                'level': 'INFO',
                'class': 'graypy.GELFHandler',
                'host': GELF_IP_ADDRESS,
                'port': GELF_PORT,
                'formatter': 'simple',
            },
        }
    )
