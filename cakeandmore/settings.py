"""
إعدادات مشروع Django - Cake & More 🍰 (جاهز للنشر على Render + Cloudinary)
"""

from pathlib import Path
import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ==============================
# 📁 المسارات الأساسية
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================
# ⚙️ إعدادات الأمان والتصحيح
# ==============================
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-temp-key-for-dev")
DEBUG = os.environ.get("DEBUG", "True") == "True"

# عند النشر على Render، أضف اسم النطاق إلى ALLOWED_HOSTS
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".onrender.com"]


# ==============================
# 🧩 التطبيقات المثبتة
# ==============================
INSTALLED_APPS = [
    # Django الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'core',
    'store',
    'orders',

    # التخزين السحابي
    'cloudinary',
    'cloudinary_storage',
]


# ==============================
# 🔒 الميدل وير
# ==============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cakeandmore.urls'


# ==============================
# 🧱 إعداد القوالب
# ==============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
# 🗄️ قاعدة البيانات (محلية + Render)
# ==============================
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}


# ==============================
# 🔐 تحقق كلمات المرور
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
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ==============================
# 🎨 الملفات الثابتة (Static)
# ==============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# دعم Render لجمع الملفات تلقائيًا
if os.environ.get('RENDER'):
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# ==============================
# ☁️ Cloudinary - تخزين الملفات الإعلامية
# ==============================
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME', 'dnufu22om'),
    api_key=os.environ.get('CLOUDINARY_API_KEY', '113862499839368'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET', 'iDL0DtenGGMd_e_91Seb0sLyX2c')
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dnufu22om',
    'API_KEY': '113862499839368',
    'API_SECRET': 'iDL0DtenGGMd_e_91Seb0sLyX2c',
    'MEDIA_LIBRARY': 'cakeandmore',  # كل الصور تُرفع داخل هذا المجلد
}


# ==============================
# 🖼️ ملفات الميديا
# ==============================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==============================
# 🆔 المفتاح الافتراضي للنماذج
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
