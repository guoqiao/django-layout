import os
from path import Path

# path of the dir contains site level files
SITE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
SITE_NAME = SITE_DIR.name

BASE_DIR = SITE_DIR.parent
ROOT_URLCONF = '{}.urls'.format(SITE_NAME)
WSGI_APPLICATION = '{}.wsgi.application'.format(SITE_NAME)

HOME = Path(os.environ['HOME'])
DATA_ROOT = (HOME / 'data' / SITE_NAME).makedirs_p()
STATIC_ROOT = (HOME / 'static' / SITE_NAME).makedirs_p()
MEDIA_ROOT = (HOME / 'media' / SITE_NAME).makedirs_p()
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

LANGUAGES = [
    ('en', 'English'),
]

LANGUAGE_CODE = 'en'


# UTC, Pacific/Auckland, Asia/Shanghai
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',

    'apps.accounts',
    'apps.main',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

FIXTURE_DIRS = [
    BASE_DIR / 'fixtures'
]

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

AUTHENTICATION_BACKENDS = ['apps.accounts.backends.UserProxyModelBackend']

## settings needs to override in local.py
DEBUG = True

ALLOWED_HOSTS = []

SITE_URL = 'http://127.0.0.1:8000'

SECRET_KEY = '9fo+zzk+vxr0oo_og@ppmzzz7z08=a$er^r2_)ius&5lt^@*of'

ADMINS = []

MANAGERS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # put db outside repo, so you can move code dir around or delete it
        'NAME': DATA_ROOT / 'sqlite.db',
    }
}

# email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST = 'email-host'
EMAIL_HOST_USER = 'email-user-name'
EMAIL_HOST_PASSWORD = 'email-user-password'

DEFAULT_FROM_EMAIL = 'from-email'
REPLY_TO_EMAIL = 'reply-to-email'
RETURN_PATH_EMAIL = 'return-path-email'

SHELL_PLUS_PRE_IMPORTS = (
    ('datetime', '*'),
    ('path', 'Path'),
)


try:
    from .local import *  # noqa
except ImportError:
    pass
