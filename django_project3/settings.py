"""
Django settings for django_project3 project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os


#if os.name == 'nt':
 #   import platform
  #  OSGEO4W = r"C:\OSGeo4W"
   # if '64' in platform.architecture()[0]:
    #    OSGEO4W += "64"
    #assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    #os.environ['OSGEO4W_ROOT'] = OSGEO4W
    #os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"
    #os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    #os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']
    #GDAL_LIBRARY_PATH = r'C:\OSGeo4W64\bin\gdal300.dll'
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
#SECRET_KEY = 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')

#DEBUG = (os.environ.get('DEBUG_VALUE')=='True')

ALLOWED_HOSTS = ['rossdjangoawesomeapp.herokuapp.com', 'localhost', '127.0.0.1', 'localhost:8000']

#ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'django_comments',
    'shops',
    'django.contrib.gis'
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
    ]

ROOT_URLCONF = 'django_project3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'django_project3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
#}


#import dj_database_url
#DATABASES = { 'default': dj_database_url.config(
 #   default = 'postgis://tmlvmvfevgvgpy:75115f9ac5577c6cb27280e409c5a2f94b99e37fdbd246cb992d78d29ddecd32@ec2-34-194-198-176.compute-1.amazonaws.com:5432/d9ctat07r8q6pk?postgis_extension=true&search_schema_path=public,postgis'
  #      )
   # }


#import dj_database_url
#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


#DATABASES = {'default':dj_database_url.config(default='postgis://tmlvmvfevgvgpy:75115f9ac5577c6cb27280e409c5a2f94b99e37fdbd246cb992d78d29ddecd32@ec2-34-194-198-176.compute-1.amazonaws.com:5432/d9ctat07r8q6pk?postgis_extension=true&search_schema_path=public,postgis')}


#DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


#DATABASES = {


 #   'default': {
  #      'ENGINE': 'django.contrib.gis.db.backends.postgis',
   #     'NAME': 'postgres',
    #    'USER': 'postgres',
     #   'PASSWORD': 'Cobra488016',
      #  'HOST': 'localhost',
       # 'PORT': '5432'
    #}

    
#}

#DATABASES = {
    #'default': {
   #     'ENGINE': 'django.db.backends.sqlite3',
     #   'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#},

 #   'default': {
  #      'ENGINE': 'django.contrib.gis.db.backends.postgis',
   #     'NAME': 'postgres',
    #    'USER': 'postgres',
     #   'PASSWORD': 'Cobra488016',
      #  'HOST': 'localhost',
       # 'PORT': '5432'
    #}

    
#}


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








# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators



# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD =  os.environ.get('EMAIL_PASS')
EMAIL_PORT = 587

AUTHENTICATION_BACKENDS = (
    #Needed to login by username in Django admin, regardless of 'allauth'
    'django.contrib.auth.backends.ModelBackend',

    #allauth specifc authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    )

CRISPY_TEMPLATE_PACK = 'bootstrap4'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')


#AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
#AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
#AWS_STORAGE_BUCKET_NAME = 'AWS_STORAGE_BUCKET_NAME'


AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

django_heroku.settings(locals())

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '*',
        'USER': '*',
        'PASSWORD': '*',
        'HOST': '*',
        'PORT': '5432',
    },
}