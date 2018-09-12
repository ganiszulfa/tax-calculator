import os

from django.contrib.messages import constants as messages


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOW_DT = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['www.theapp.com', 'theapp.com', 'app.theapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.humanize',

    'app_modules.calculator',
]


BUILD_DIR = './bakery/public/'
BAKERY_VIEWS = () # added by each method

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


if ALLOW_DT:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
    INSTALLED_APPS += ['debug_toolbar', ]
    INTERNAL_IPS = ()
    for x in range(1, 240):
        INTERNAL_IPS += ('172.17.0.'+str(x),)
    # WARNING, check the IPS first if DT is not shown
    # get the internal ips from request.META['REMOTE_ADDR'] 

ROOT_URLCONF = 'app_core.urls'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', str(BASE_DIR)*4)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
            ],
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

WSGI_APPLICATION = 'app_core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DB_NAME = os.environ['POSTGRES_DB']
DB_USER = os.environ['POSTGRES_USER']
DB_PASS = os.environ['POSTGRES_PASSWORD']
DB_PORT = os.environ['POSTGRES_PORT']

POSTGRES_HOST = os.environ['POSTGRES_HOST']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': POSTGRES_HOST,
        'PORT': DB_PORT
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Etc/GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_REDIRECT_URL = '/dashboard/'

SITE_ID = 1

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'complete': {
            'format': '%(asctime)s %(levelname)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'complete'
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': './djangolog.log',
            'formatter': 'complete'
        },
    },
    'loggers': {
        'core.handlers': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file']
    }, 
}

def custom_show_toolbar(request):
     return request.user.is_staff 

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'app_core.settings.custom_show_toolbar',
}

handler404 = 'app_modules.landing.views.my404'
