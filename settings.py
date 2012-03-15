# Django settings for lyrics project.

import os

PROJECT_PATH = os.path.abspath(os.path.split(__file__)[0])

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates"),
    )

DEBUG = True
TEMPLATE_DEBUG = DEBUG

#MANAGERS = ADMINS

#DATABASE_ENGINE = 'sqlite3'
#
#DATABASE_NAME = os.path.join(PROJECT_PATH, 'lyrics.db')

DATABASE_ENGINE = 'mysql'

DATABASE_NAME = 'lyrione'

DATABASE_USER = 'lyrione'

DATABASE_PASSWORD = 'aqwsderf'

DATABASE_HOST = '81.177.33.114'

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = ''

MEDIA_URL = './media/'

STATIC_ROOT = ''

STATIC_URL = os.path.join(PROJECT_PATH, 'static')

ARTISTS_URL = os.path.join(PROJECT_PATH, 'artists')

ALBUMS_URL = os.path.join(PROJECT_PATH, 'albums')

ADMIN_MEDIA_PREFIX = os.path.join(PROJECT_PATH, 'media')

STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ogl9(!_%=l=wmwe#_ws@0&t2)#2!lvvvf(8)46e&x91)_*w-ul'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    )

ROOT_URLCONF = 'urls'

#TEMPLATE_DIRS = 'templates'

HAYSTACK_SITECONF = 'main.search'

HAYSTACK_SEARCH_ENGINE = 'whoosh'

search_directory = os.path.join(PROJECT_PATH, 'search')
#print search_directory
HAYSTACK_WHOOSH_PATH = search_directory

#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#        },
#    }

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'haystack',
    'main',
    'south',
    )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

