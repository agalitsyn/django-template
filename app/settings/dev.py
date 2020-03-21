import os

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
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
