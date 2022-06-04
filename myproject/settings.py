"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a%b7(7*f-)3p^9l(uzkj$ic-32)bd9=0)24te70@4l07(2jgv+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'adminlte3',
    'adminlte3_theme',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # local
    "accounts.apps.AccountsConfig",
    "airlines.apps.AirlinesConfig",
    "passangers.apps.PassangersConfig",
    "hotels.apps.HotelsConfig",
    "core.apps.CoreConfig",
    "jobs.apps.JobsConfig",
    "blog.apps.BlogConfig",
    "profiles.apps.ProfilesConfig",
    # third
    "widget_tweaks",
    "django_extensions",
    "braces",
    "azbankgateways"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                # local
                'core.context_processors.access_setting',
            ],
        },
    },
]
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'admin',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATICFILES_DIRS = [
    BASE_DIR / "assets",
]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static_cdn" / "static"

MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "static_cdn" / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.User"
LANGUAGE_CODE = "en-us"

AZ_IRANIAN_BANK_GATEWAYS = {
    "GATEWAYS": {
        "BMI": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
            "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
            "SECRET_KEY": "<YOUR SECRET CODE>",
        },
        "SEP": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
            "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
        },
        "ZARINPAL": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        },
        "IDPAY": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
            "METHOD": "POST",  # GET or POST
            "X_SANDBOX": 0,  # 0 disable, 1 active
        },
        "ZIBAL": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        },
        "BAHAMTA": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        },
        "MELLAT": {
            "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
            "USERNAME": "<YOUR USERNAME>",
            "PASSWORD": "<YOUR PASSWORD>",
        },
    },
    "IS_SAMPLE_FORM_ENABLE": True,  # ??????? ? ??? ??? ??? ???? ???
    "DEFAULT": "BMI",
    "CURRENCY": "IRR",  # ???????
    "TRACKING_CODE_QUERY_PARAM": "tc",  # ???????
    "TRACKING_CODE_LENGTH": 16,  # ???????
    "SETTING_VALUE_READER_CLASS": "azbankgateways.readers.DefaultReader",  # ???????
    "BANK_PRIORITIES": [
        "BMI",
        "SEP",
        # and so on ...
    ],  # ???????
}



