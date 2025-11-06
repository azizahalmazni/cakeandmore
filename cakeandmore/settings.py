"""
إعدادات مشروع Django - Cake & More 🍰
"""

from pathlib import Path
import os

# ==============================
# 📁 المسارات الأساسية (BASE_DIR)
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# ⚙️ إعدادات الأمان والتصحيح
# ==============================
SECRET_KEY = 'django-insecure-#3$p@n2dmd!+heoi25&ilmx*bfj4s!+prfaf(79k8!27x(@$di'

DEBUG = True

ALLOWED_HOSTS = []


# ==============================
# 🧩 التطبيقات المثبتة (INSTALLED_APPS)
# ==============================
INSTALLED_APPS = [
    # تطبيقات Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع الأساسية 🍰
    'core',      # الصفحات العامة (الرئيسية، التواصل، التسجيل...)
    'store',     # المنتجات والعربة
    'orders',    # الطلبات والدفع
]


# ==============================
# 🔒 الميدل وير (Middleware)
# ==============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # لدعم اللغة العربية
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==============================
# 📂 إعدادات القوالب (Templates)
# ==============================
ROOT_URLCONF = 'cakeandmore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # 🔹 المجلد الرئيسي للقوالب (templates)
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

WSGI_APPLICATION = 'cakeandmore.wsgi.application'


# ==============================
# 🗄️ إعدادات قاعدة البيانات (Database)
# ==============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==============================
# 🔐 تحقق كلمات المرور (Password Validation)
# ==============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==============================
# 🌍 اللغة والمنطقة الزمنية
# ==============================
LANGUAGE_CODE = 'ar'           # اللغة العربية
TIME_ZONE = 'Asia/Riyadh'      # التوقيت المحلي للرياض
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ==============================
# 🎨 الملفات الثابتة (Static Files)
# ==============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # مجلد الملفات الثابتة داخل المشروع
STATIC_ROOT = BASE_DIR / 'staticfiles'    # مجلد تجميع الملفات الثابتة عند النشر


# ==============================
# 🖼️ الملفات الإعلامية (Media Files)
# ==============================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==============================
# 🆔 المفتاح الافتراضي للحقل الأساسي
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
