from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['developerpe.herokuapp.com']
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd25i063gce88cj',
        'USER': 'hemvrjpefiaflv',
        'PASSWORD': '6d45ea769ca2ca6f9bf14eed3129a16f97d21c7ea57b42308d894e181eb52286',
        'HOST': 'ec2-23-21-147-71.compute-1.amazonaws.com',
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
