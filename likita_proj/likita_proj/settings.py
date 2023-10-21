import dj_database_url
from pathlib import Path
import os, environ
from datetime import datetime
env = environ.Env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
environ.Env.read_env()

environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY= env('SECRET_KEY', default='bjhvuovlbgcvotuvjvtgctuovgvtvuvghkvtvyulv')

# # SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False) == True


ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(" ")


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'cloudinary_storage',
    'cloudinary',
    
    'base.apps.BaseConfig',
    'authy.apps.AuthyConfig',
    'chat.apps.ChatConfig',
    'clinic.apps.ClinicConfig',
    'profiles.apps.ProfilesConfig',
    'liki_api.apps.LikiApiConfig',
    
    
    'fontawesomefree',
    'bootstrap5',
    'rest_framework',
    'corsheaders',
    'channels',
    
    "verify_email.apps.VerifyEmailConfig",
    
    'django_bleach',
    'django_quill',
]

AUTH_USER_MODEL = 'base.User'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

# for django v4.2+ use the below storage settings
# STORAGES = {
#     "default": {
#         "BACKEND": "django.core.files.storage.FileSystemStorage",
#     },
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

# for < django  v4.2, use this storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# WHITENOISE_MANIFEST_STRICT = False

# allow react app to use this projects api as endpoint
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000'
]

ROOT_URLCONF = 'likita_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [os.path.join(  BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'likita_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# database_url = env("DATABASE_URL")
# DATABASES = {
#      'default' :  dj_database_url.parse(
#      database_url,
#      conn_max_age=600,
#      conn_health_checks=True,
   
#  )
#  }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': env('DATABASE_PW'),
#         'HOST': 'containers-us-west-47.railway.app',
#         'PORT': '7954'

#     }
# }

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'dokto',
       'USER': 'postgres',
       'PASSWORD': 'Omolabake1',
       'HOST': 'localhost',
   }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True
    
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'media')

if  env("ENVIRONMENT") == "PRODUCTION":
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    
    
CLOUDINARY_STORAGE = {
    'CLOUD_NAME' : env('MEDIA_CLOUD_NAME'),
    'API_KEY' : env('MEDIA_CLOUD_API_KEY'),
    'API_SECRET' : env('MEDIA_CLOUD_API_SECRET')
}

LOGIN_URL = 'login'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# email host server configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_ID') 
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PW')

DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'
EMAIL_PAGE_DOMAIN = 'https://www.dokto.com.ng/'


# link expres
EXPIRE_AFTER = "7d" # Will expire after seven day from link generation
MAX_RETRIES = 100

SUBJECT = f'Activate Your DRKAYMD account'
REQUEST_NEW_EMAIL_TEMPLATE='authy/request_new_email.html'
HTML_MESSAGE_TEMPLATE = "authy/email_message.html"

VERIFICATION_SUCCESS_TEMPLATE = "authy/success.html"
VERIFICATION_FAILED_TEMPLATE = "authy/failed.html"
LINK_EXPIRED_TEMPLATE = 'authy/expired.html'
NEW_EMAIL_SENT_TEMPLATE  = 'authy/new_email_sent.html'
