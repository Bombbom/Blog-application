from .base import *
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB_NAME'),
        'USER': config('POSTGRES_DB_USER'),
        'PASSWORD': config('POSTGRES_DB_PASSWORD'),
        'HOST': config('POSTGRES_DB_HOST'),
        'PORT': config('POSTGRES_DB_PORT'),
    }
}