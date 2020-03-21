from os import environ

from split_settings.tools import include, optional

# Managing environment via DJANGO_ENV variable:
environ.setdefault('DJANGO_ENV', 'dev')
ENV = environ['DJANGO_ENV']

base_settings = [
    'settings.py',
    # Select the current env:
    '{0}.py'.format(ENV),
    # Optionally override some settings:
    optional('local.py'),
]

# Include settings:
include(*base_settings)
