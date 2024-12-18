"""
Django settings for DjangoProject1 project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path # Import path management module
#############################################################################################################

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOGIN_URLS = ['/candidate/login','']  # URLS to the login views

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] # Whitelist

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth', # Authentication App
    'django.contrib.contenttypes', # Content Type App
    'django.contrib.sessions', # Sessions management App
    'django.contrib.messages', # Messages management App
    'django.contrib.staticfiles', # Static files management App
    'django.contrib.admin', # Admin user management App
    'visitor', # Visitors management app
    'candidate.apps.CandidateConfig' # Candidates management app
]

# List of the backends used for authentication
AUTHENTICATION_BACKENDS = [
    'candidate.backends.ApplicationAuthBackend',
]

# Middlewares used by the project
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware', # Middleware that manages sessions
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Middleware that manages authentication
    'candidate.middleware.LoginRequiredMiddleware', # Middleware that manages login requirements
    'django.middleware.security.SecurityMiddleware', # Middleware that manages the security of the project
    'django.middleware.common.CommonMiddleware', # Common Middleware
    'django.middleware.csrf.CsrfViewMiddleware', # Middleware that manages CSRF tokens
    'django.contrib.messages.middleware.MessageMiddleware', # Middleware that manages messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Middleware that protect the project against clickjacking
]

# Default URL configuration file
ROOT_URLCONF = 'DjangoProject1.urls'

# Template Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # Backend used for the templates
        'DIRS': [BASE_DIR / 'templates'], # Directory that contains the templates
        'APP_DIRS': True, # Search for the templates directly in the app
        'OPTIONS': { # Templates options
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoProject1.wsgi.application' # WSGI of the applications

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': { # Default Database
        'ENGINE': 'django.db.backends.mysql', # Engine used by the DB
        'NAME': '', # Name of the DB
        'USER': '', # Username to connect to the DB
        'PASSWORD': '', # Password to connect to the DB
        'HOST': '', # Address of the DB
        'PORT': '', # Port to access the DB
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [ # List of the validators available to check the passwords
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
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/' # Path to the static resources repository
STATICFILES_DIRS = [BASE_DIR / 'DjangoProject1/static'] # Absolute path to the static resources repository

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
