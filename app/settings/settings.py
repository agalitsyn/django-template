import os

from decouple import config
from django.conf.locale.ru import formats as ru_formats

WSGI_APPLICATION = 'app.wsgi.application'
ROOT_URLCONF = 'app.urls'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-SITE_ID
SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    # Custom apps
    'app.components.main',
    'app.components.extensions',

    # Third party apps
    'django_extensions',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            # Contains plain text templates, like `robots.txt`:
            os.path.join(BASE_DIR, 'templates')
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.i18n',
                'django.template.context_processors.tz',
            ],
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = ('ru',)
LANGUAGE_CODE = config('DJANGO_LANGUAGE_CODE', default='ru')
TIME_ZONE = config('DJANGO_TIME_ZONE', default='UTC')
LOCALE_PATHS = (os.path.join(BASE_DIR, '..', 'assets', 'locale'),)
# Formats
ru_formats.DATETIME_FORMAT = "d/m/y H:i"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'assets', 'static')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'assets', 'node_modules'),
)

MEDIA_ROOT = config('DJANGO_MEDIA_ROOT', default=os.path.join(BASE_DIR, '..', 'media'))
MEDIA_URL = '/media/'

# Fix: The number of GET/POST parameters exceeded settings.DATA_UPLOAD_MAX_NUMBER_FIELDS
# https://docs.djangoproject.com/en/3.0/ref/settings/#data-upload-max-number-fields
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000
# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-DATA_UPLOAD_MAX_MEMORY_SIZE
DATA_UPLOAD_MAX_MEMORY_SIZE = 2147483648 # 2GB

# Security
# https://docs.djangoproject.com/en/2.2/topics/security/
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Email
# https://docs.djangoproject.com/en/3.0/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
