"""
Django settings for esr21 project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import configparser
import os
from pathlib import Path
import sys

from django.core.management.color import color_style

# from .logging import LOGGING
style = color_style()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = 'esr21'
SITE_ID = 40

REVIEWER_SITE_ID = 1

ETC_DIR = os.path.join('/etc/', APP_NAME)

LOGIN_REDIRECT_URL = 'home_url'

INDEX_PAGE = 'esr21.bhp.org.bw:8000'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

CONFIG_FILE = f'{APP_NAME}.ini'

CONFIG_PATH = os.path.join(ETC_DIR, CONFIG_FILE)
sys.stdout.write(style.SUCCESS(f'  * Reading config from {CONFIG_FILE}\n'))
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['django'].get('secret_key', 'blah$blah$blah')

# KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')

LIVE_SYSTEM = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'esr21.bhp.org.bw', '127.0.0.1']

# email configurations
EMAIL_BACKEND = config['email_conf'].get('email_backend')
EMAIL_HOST = config['email_conf'].get('email_host')
EMAIL_USE_TLS = config['email_conf'].get('email_use_tls')
EMAIL_PORT = config['email_conf'].get('email_port')
EMAIL_HOST_USER = config['email_conf'].get('email_user')
EMAIL_HOST_PASSWORD = config['email_conf'].get('email_host_pwd')
DEFAULT_FROM_EMAIL = config['email_conf'].get('email_user')

SESSION_EXPIRE_SECONDS = 1800

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'django_countries',
    'rest_framework',
    'django_js_reverse',
    'rest_framework.authtoken',
    'crispy_forms',
    'chartjs',
    'django_crypto_fields.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'edc_calendar.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_lab_dashboard.apps.AppConfig',
    'edc_model_admin.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_call_manager.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'esr21_follow.apps.AppConfig',
    'esr21_export.apps.AppConfig',
    'esr21_dashboard.apps.AppConfig',
    'esr21_labs.apps.AppConfig',
    'esr21_prn.apps.AppConfig',
    'esr21_subject.apps.AppConfig',
    'esr21_metadata_rules.apps.AppConfig',
    'esr21_reference.apps.AppConfig',
    'esr21_visit_schedule.apps.AppConfig',
    'esr21.apps.EdcAppointmentAppConfig',
    'esr21.apps.EdcLabAppConfig',
    'esr21.apps.EdcBaseAppConfig',
    'esr21.apps.EdcDataManagerAppConfig',
    'esr21.apps.EdcFacilityAppConfig',
    'esr21.apps.EdcLocatorAppConfig',
    'esr21.apps.EdcMetadataAppConfig',
    'esr21.apps.EdcProtocolAppConfig',
    'esr21.apps.EdcVisitTrackingAppConfig',
    'esr21.apps.EdcTimepointAppConfig',
    'esr21.apps.EdcDeviceAppConfig',
    'esr21.apps.EdcLabelAppConfig',
    'esr21.apps.EdcSyncAppConfig',
    'esr21.apps.EdcSyncFilesAppConfig',
    'esr21.apps.EdcSenaiteInterfaceAppConfig',
    'esr21.apps.AppConfig',
    'esr21_reports.apps.AppConfig',

]
BOOTSTRAP3 = {
    'include_jquery': True,
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
    'edc_lab_dashboard.middleware.DashboardMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',

]

ROOT_URLCONF = 'esr21.urls'

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

WSGI_APPLICATION = 'esr21.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
mysql_config = configparser.ConfigParser()
mysql_config.read(os.path.join(ETC_DIR, 'mysql.ini'))

HOST = mysql_config['mysql']['host']
DB_USER = mysql_config['mysql']['user']
DB_PASSWORD = mysql_config['mysql']['password']
DB_NAME = mysql_config['mysql']['database']
PORT = mysql_config['mysql']['port']

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': DB_NAME,
         'USER': DB_USER,
         'PASSWORD': DB_PASSWORD,
         'HOST': HOST,  # Or an IP Address that your DB is hosted on
         'PORT': PORT,
     }
 }

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('tn', 'Setswana'),
    ('en', 'English'),
)

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = False

USE_TZ = True
USE_L10N = False
DATETIME_INPUT_FORMATS = ['%d/%B/%Y %H:%M']
DATE_INPUT_FORMATS = ["%d %B %Y"]
TIME_INPUT_FORMATS = ['%H:%M']
DATETIME_FORMAT = 'd/M/Y H:i'
DATE_FORMAT = 'd/M/Y'
SHORT_DATE_FORMAT = 'd/M/Y'
SHORT_DATETIME_FORMAT = 'd/M/Y H:i'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'esr21', 'static')

HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')

CUPS_SERVERS = 'localhost'
LABEL_PRINTER = 'esr21_printer'
LABEL_TEMPLATE_FOLDER = os.path.join(STATIC_ROOT, 'esr21_label', 'label_templates')

# dashboards
DASHBOARD_URL_NAMES = {
    'screening_listboard_url': 'esr21_dashboard:screening_listboard_url',
    'subject_listboard_url': 'esr21_dashboard:subject_listboard_url',
    'subject_dashboard_url': 'esr21_dashboard:subject_dashboard_url',
    'data_manager_listboard_url': 'edc_data_manager:data_manager_listboard_url',
    'export_listboard_url': 'esr21_export:export_listboard_url',
    'esr21_follow_listboard_url': 'esr21_follow:esr21_follow_listboard_url',
    'esr21_follow_appt_listboard_url': 'esr21_follow:esr21_follow_appt_listboard_url',
    'esr21_follow_booking_listboard_url': 'esr21_follow:esr21_follow_booking_listboard_url',
    'esr21_follow_book_listboard_url': 'esr21_follow:esr21_follow_book_listboard_url',
    'esr21_reports_home_url': 'esr21_reports:esr21_reports_home_url',
}

LAB_DASHBOARD_BASE_TEMPLATES = {}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'esr21/base.html',
    'dashboard_base_template': 'esr21/base.html',
    'subject_dashboard_template': 'esr21_dashboard/subject/dashboard.html',
    'screening_listboard_template': 'esr21_dashboard/screening/listboard.html',
    'subject_listboard_template': 'esr21_dashboard/subject/listboard.html',
    'export_listboard_template': 'esr21_export/listboard.html',
    'data_manager_listboard_template': 'edc_data_manager/listboard.html',
    'esr21_follow_listboard_template': 'esr21_follow/follow_listboard.html',
    'esr21_follow_appt_listboard_template': 'esr21_follow/appointments_windows_listboards.html',
    'esr21_follow_booking_listboard_template': 'esr21_follow/bookings_listboard.html',
    'esr21_follow_book_listboard_template': 'esr21_follow/book_listboard.html',
}

# edc_facility
COUNTRY = 'botswana'

PARENT_REFERENCE_MODEL1 = ''
PARENT_REFERENCE_MODEL2 = ''

DEVICE_ID = config['edc_device'].get('device_id', '99')
DEVICE_ROLE = config['edc_device'].get('role')

EDC_SYNC_SERVER_IP = config['edc_sync'].get('server_ip')
EDC_SYNC_FILES_REMOTE_HOST = config['edc_sync_files'].get('remote_host')
EDC_SYNC_FILES_USER = config['edc_sync_files'].get('sync_user')
EDC_SYNC_FILES_USB_VOLUME = config['edc_sync_files'].get('usb_volume')
