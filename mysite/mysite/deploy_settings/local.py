from .base import *
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB_NAME', default='postgres'),
        'USER': config('POSTGRES_DB_USER', default='postgres'),
        'PASSWORD': config('POSTGRES_DB_PASSWORD', default='postgres'),
        'HOST': config('POSTGRES_DB_HOST', default='db'),
        'PORT': config('POSTGRES_DB_PORT', default=5432),
    }
}