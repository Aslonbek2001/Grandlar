from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-83p+tgqvg4xo1hbn22rpofna@8&mr098pgzon-*r43y^n^x11q'
DEBUG = False
ALLOWED_HOSTS = [
    "*"
]

INSTALLED_APPS = [
    'jazzmin', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'application', # Ariza yuborish uchun
    'main', # Qo'shimcha Statistika va shunga o'xshash ma'lumotlar uchun
    'employee', # Xodimlar bilan ishlash agar kerak bo'lsa
    'student', # Hemis login, data studentlar uchun
    'users'
]
AUTH_USER_MODEL = 'users.User'

CSRF_TRUSTED_ORIGINS = [
    "https://grand.uzgeouniver.uz",  # https bo‘lishi kerak
    "http://grand.uzgeouniver.uz",   # agar faqat http bo‘lsa
]

CLIENT_ID = 3
CLIENT_SECRET = 'P6BJGjhsilgzlyqMlvftWxKZ49UT1E0NhFKlVIec'
REDIRECT_URI = "https://grand.uzgeouniver.uz/student/data/"
AUTHORIZE_URL = "https://student.uzgeouniver.uz/oauth/authorize"
TOKEN_URL = "https://student.uzgeouniver.uz/oauth/access-token"
RESOURCE_OWNER_URL = "https://student.uzgeouniver.uz/oauth/api/user?fields="


LOGIN_REDIRECT_URL = '/admin/'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
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

WSGI_APPLICATION = 'core.wsgi.application'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "grandlar",
        "USER": "grandlar",
        "PASSWORD": "12345",
        "HOST": "localhost",
        "PORT": "5432",
    }
}



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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
