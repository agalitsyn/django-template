import os

from decouple import config

from app.settings.settings import INSTALLED_APPS, MIDDLEWARE, BASE_DIR


DEBUG = True

SECRET_KEY = 'dev-secret-key'

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
# Allow debug() in templates
INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

db_settings = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
}
if config('DJANGO_POSTGRES_DB', default='') != "":
    db_settings = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DJANGO_POSTGRES_DB',),
        'USER': config('DJANGO_POSTGRES_USER'),
        'PASSWORD': config('DJANGO_POSTGRES_PASSWORD'),
        'HOST': config('DJANGO_POSTGRES_HOST'),
        'PORT': config('DJANGO_POSTGRES_PORT', cast=int, default=5432),
        'CONN_MAX_AGE': config('DJANGO_POSTGRES_CONN_MAX_AGE', cast=int, default=60),
        'OPTIONS': {
            'connect_timeout': config('DJANGO_POSTGRES_CONN_TIMEOUT', cast=int, default=60),
        },
    }

DATABASES = {
    'default': db_settings,
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


def custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return request.user.is_superuser


# Django debug toolbar:
# https://django-debug-toolbar.readthedocs.io
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK':
        'app.settings.dev.custom_show_toolbar',
}
