"""
Local settings for ecobasa project
"""

from __future__ import unicode_literals
from .default_settings import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ecobasa.sql',
    },
}

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
    'postman': 'postman.south_migrations',
}

FIXTURE_DIRS = (
   os.path.abspath(os.path.join(os.path.dirname( __file__ ),
                                'ecobasa',
                                'fixtures')),
)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'r(y6&k-^j^lz2_)bpt&89v2aqy=2c%f^ppff2v5fptk%a11*_!'

SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
