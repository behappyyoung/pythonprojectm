"""
Django settings for hellodjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
##BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jdvmyjujy$39^54u=c(16ota@rb7qp%n196rrkbz1vs0and_5z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'meals',
    'userena',
    'guardian',
    'easy_thumbnails',
    'accounts',
    'sitetree',
    'django_messages',
    'pipeline',
    'less',
    'twitter_bootstrap',
    'djangular',
)

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'accounts.MyProfile'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
)

ROOT_URLCONF = 'djangotest.urls'

WSGI_APPLICATION = 'djangotest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'projectm',
        'USER': 'projectm',
        'PASSWORD': 'projectm',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

my_app_less = os.path.join(BASE_DIR, 'my_app', 'static', 'less')

# For apps outside of your project, it's simpler to import them to find their root folders
import twitter_bootstrap
bootstrap_less = os.path.join(os.path.dirname(twitter_bootstrap.__file__), 'static', 'less')

PIPELINE_LESS_ARGUMENTS = u'--include-path={}'.format(os.pathsep.join([bootstrap_less, my_app_less]))


PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

## pipe line
PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
            'twitter_bootstrap/less/bootstrap.less',
        ),
        'output_filename': 'css/b.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'bootstrap': {
        'source_filenames': (
          'twitter_bootstrap/js/transition.js',
          'twitter_bootstrap/js/modal.js',
          'twitter_bootstrap/js/dropdown.js',
          'twitter_bootstrap/js/scrollspy.js',
          'twitter_bootstrap/js/tab.js',
          'twitter_bootstrap/js/tooltip.js',
          'twitter_bootstrap/js/popover.js',
          'twitter_bootstrap/js/alert.js',
          'twitter_bootstrap/js/button.js',
          'twitter_bootstrap/js/collapse.js',
          'twitter_bootstrap/js/carousel.js',
          'twitter_bootstrap/js/affix.js',
        ),
        'output_filename': 'js/b.js',
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


##STATIC_ROOT = (os.path.join(os.path.dirname(__file__), '..', 'djangotest/static'))
##STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
##STATICFILES_DIRS = ( os.path.join(BASE_DIR, "staticfiles"),    STATIC_URL,)

# Static asset configuration
STATIC_URL = '/static/'
##STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
##STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
##STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)





##MEDIA_ROOT = BASE_DIR
MEDIA_ROOT = ''
############# addded for heroku ###########################

# Parse database configuration from $DATABASE_URL
import dj_database_url
###DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'yourgmailaccount@gmail.com'
EMAIL_HOST_PASSWORD = 'yourgmailpassword'


USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
TEMPLATE_LOADERS =('django.template.loaders.filesystem.Loader',
 'django.template.loaders.app_directories.Loader')

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
'django.core.context_processors.request',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}
