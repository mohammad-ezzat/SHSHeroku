"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
#import django_heroku
import dj_database_url
WHITENOISE_USE_FINDERS = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/pwa', 'serviceworker.js')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8kcq6pxq1b6x_u15n15^=se4o3qu1l+thk+%3i7*c-c6w78jfo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["https://smart-hospital-system.herokuapp.com/"
,"localhost","127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    # my apps
    'whitenoise.runserver_nostatic',
    'user.apps.UserConfig',
    'xpatient.apps.XpatientConfig',
    
    'xstaff.apps.XstaffConfig',
    'xstaff_doctor.apps.XstaffDoctorConfig',
    'xstaff_hr.apps.XstaffHrConfig',
    'xstaff_secretary.apps.XstaffSecretaryConfig',
    
    'y_service.apps.YServiceConfig',
    'ys_appointment.apps.YsAppointmentConfig',
    'ys_blood_bank.apps.YsBloodBankConfig',
    'ys_laboratory.apps.YsLaboratoryConfig',
    'ys_pharmacy.apps.YsPharmacyConfig',
    'ys_x_ray.apps.YsXRayConfig',
    
    'rest_framework',
    'crispy_forms',
     
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Progressive web application
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
                ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'
AUTH_USER_MODEL = 'user.MyUser'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'project/static',
]


MEDIA_URL =  '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Activate Django-Heroku
#django_heroku.settings(locals())


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL  = '/'
LOGOUT_REDIRECT_URL = '/'


#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER ='smarthospitalsystem2022@gmail.com'
EMAIL_HOST_PASSWORD ='hifckphfjffbtbbq'
EMAIL_USE_TLS = True
EMAIL_PORT = '587'


# PWA manifest configuration

PWA_APP_NAME = 'SHS'
PWA_APP_DESCRIPTION = "SHS"
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
	{
        "src": "static/icons/manifest-icon-192.maskable.png",
        "sizes": "192x192"
    }
]
PWA_APP_ICONS_APPLE = [
	{
		"src": "static/icons/manifest-icon-192.maskable.png",
        "sizes": "192x192"
	}
]
PWA_APP_SPLASH_SCREEN = [
	{
		'src': 'static/icons/manifest-icon-512.maskable.png',
		'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
	}
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

