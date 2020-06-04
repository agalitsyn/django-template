from decouple import config, Csv


# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

DEBUG = False

SECRET_KEY = config('DJANGO_SECRET_KEY')

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=Csv())

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DJANGO_POSTGRES_DB'),
        'USER': config('DJANGO_POSTGRES_USER'),
        'PASSWORD': config('DJANGO_POSTGRES_PASSWORD'),
        'HOST': config('DJANGO_POSTGRES_HOST'),
        'PORT': config('DJANGO_POSTGRES_PORT', cast=int, default=5432),
        'CONN_MAX_AGE': config('DJANGO_POSTGRES_CONN_MAX_AGE', cast=int, default=60),
        'OPTIONS': {
            'connect_timeout': config('DJANGO_POSTGRES_CONN_TIMEOUT', cast=int, default=60),
        },
    },
}

# Cache
DEFAULT_CACHE = {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    'LOCATION': 'unique-snowflake',
    'TIMEOUT': 60,
    'OPTIONS': {
        'MAX_ENTRIES': 1000
    }
}
memcached_hosts = config('DJANGO_MEMCACHED_HOSTS', default="", cast=Csv())
if memcached_hosts:
    DEFAULT_CACHE = {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': memcached_hosts,
        'OPTIONS': {
            'binary': True,
            'behaviors': {
                'ketama': True,
            }
        }
    }
CACHES = {
    'default': DEFAULT_CACHE
}
CACHE_MIDDLEWARE_SECONDS = 60
