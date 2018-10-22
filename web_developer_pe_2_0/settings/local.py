from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'developer',
        'USER': 'oliver',
        'PASSWORD': 'yugiho2000',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

"""

JET_DEFAULT_THEME = 'light-violet'
JET_SIDE_MENU_COMPACT = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))
MEDIA_URL = '/media/'
STATICFILES_DIRS=[
	os.path.join(os.path.dirname(BASE_DIR),'static'),
		]

AUTH_USER_MODEL = 'usuarios.User'
CKEDITOR_UPLOAD_PATH = "uploads/"





CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}
