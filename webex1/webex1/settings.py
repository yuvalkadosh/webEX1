"""
Django settings for webex1 project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import json



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eqz_@a8(@d3$#z_#pwuuu2yd_bo=p_xyeqfl%o*^=-=g=302$2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'accounts',
    'boards',
    'widget_tweaks',
    'sslserver',
    'axes',
]

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
]


SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'webex1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
                'form_tags': 'boards.templatetags.form_tags',
            },
        },
    },
]

WSGI_APPLICATION = 'webex1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Import json configuration file
f = open('config.json')

config_file = json.load(f)

if config_file['complex_categories'] > 4:
    config_file['complex_categories'] = 4

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    #checks the similarity between the password and a set of attributes of the user.
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    #the password meets a minimum length.
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': config_file['password_min_length'], }
    },
    #checks whether the password occurs in a list of common passwords.
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    #checks whether the password isn’t entirely numeric.
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    #checks the passwords history
    {
        'NAME': 'webex1.validators.HistoryValidator',
        'OPTIONS': {
            'last_pass_amount': config_file['last_pass_amount'], },
    },
    #checks the password complexity
    {
        'NAME': 'webex1.validators.ComplexValidator',
        'OPTIONS': {
            'categories_amount': config_file['complex_categories'], },
    },
    #checks the password isnt from the dictionary
    {
        'NAME': 'webex1.validators.DictValidator',
        'OPTIONS': {
            'dict_path': config_file['password_dict_path'], },
    },

]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECURE_SSL_REDIRECT = True

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'comunicationltd10@gmail.com'
EMAIL_HOST_PASSWORD = 'Aa12345678!'
EMAIL_USE_TLS = True

#Axes
AXES_ONLY_USER_FAILURES = True
AXES_COOLOFF_TIME = 1
AXES_FAILURE_LIMIT = config_file['login_max_retries']
AXES_RESET_ON_SUCCESS = True