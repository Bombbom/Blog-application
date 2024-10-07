from .base import * 
DEBUG = True 
ADMINS = [
    
]

# ALLOWED_HOSTS = ['*']

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

## Redis settings

# REDIS_URL = 'redis://cache:6379'
# CACHES['default']['LOCATION'] = REDIS_URL
# CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]


# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True