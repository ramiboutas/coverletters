"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = str(os.environ.get('DEBUG')) == '1'
PRODUCTION = str(os.environ.get('PRODUCTION')) == '1'


ALLOWED_HOSTS = ["coverletters.ramiboutas.com"]

# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # my apps
    'coverletters',
    'texfiles.apps.TexfilesConfig',

    # third-party apps
    'django_htmx',
    'django_tex',
    'django_celery_beat',
    'django_celery_results',
    'celery_progress',
    'rosetta',
    'session_cleanup',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'utils.context_processors.coverletters',
            ],
        },
    },
    {
        'NAME': 'tex',
        'BACKEND': 'django_tex.engine.TeXEngine',
        'DIRS': (BASE_DIR.joinpath('media'),),
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'texfiles.environment.my_environment',
        }
    },
]

# LATEX_INTERPRETER = 'pdflatex'
# pdflatex, latex, xelatex, lualatex

# LATEX_GRAPHICSPATH = os.path.join(BASE_DIR, 'media/uploads')
# LATEX_INTERPRETER_OPTIONS = '-interaction=nonstopmode'

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Migrating data from SQlite to PostgreSQL | Django
# https://www.youtube.com/watch?v=BGEEzjGadYI

USE_SQLITE3_DB = str(os.environ.get('USE_SQLITE3_DB')) == '1'

POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_TESTS_DB = os.environ.get('POSTGRES_TESTS_DB')

if USE_SQLITE3_DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',}}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': POSTGRES_DB,
            'USER': POSTGRES_USER,
            'PASSWORD': POSTGRES_PASSWORD,
            'HOST': POSTGRES_HOST,
            'PORT': POSTGRES_PORT,
            'TEST': {
             'NAME': 'test_db',
             },
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGE_COOKIE_NAME = 'client_language'

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)

LOCALE_PATHS = (
    BASE_DIR.joinpath('locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static_dev",
]
STATIC_ROOT = str(BASE_DIR.joinpath('static')) # for production

# Media files
MEDIA_ROOT = BASE_DIR.joinpath('media')
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# celery
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'django-db'


# session cleanup
SESSION_COOKIE_AGE = 604800 # 1 week

from session_cleanup.settings import weekly_schedule
CELERYBEAT_SCHEDULE = {
    'session_cleanup': weekly_schedule
}


# cleanup unmodified coverletters every hour

CELERY_BEAT_SCHEDULE = {
      'scheduled_task': {
        'task': 'coverletters.tasks.cleanup_unmodified_coverletters',
        'schedule': 3600.0,
        # 'args': (16, 16),
        'options': {
            'expires': 15.0,
        },
    },
}



SITE_NAME = _('Cover letters')
META_KEYWORDS = _('coverletters, coverletter, motivationletters, motivationletter, career, job, search, career, shifting')
META_DESCRIPTION = _('In this site you can create for FREE up to 50 personalized cover letters within 10 Minutes without needing to register')



if PRODUCTION or not DEBUG:
    ALLOWED_HOSTS += ['95.90.195.163', 'anschreiben24.com', 'www.anschreiben24.com', 'cartasdemotivacion.com', 'www.cartasdemotivacion.com', 'www.coverletters.online', 'coverletters.online', 'www.motivationletters.online', 'motivationletters.online']
    # https
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_HSTS_SECONDS = 31536000 #31536000 # usual: 31536000 (1 year)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True
    PREPEND_WWW = True
