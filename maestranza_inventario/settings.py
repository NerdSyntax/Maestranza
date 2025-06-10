from pathlib import Path
from decouple import config, Csv
import sys


BASE_DIR = Path(__file__).resolve().parent.parent


# 🔐 Secret Key & Debug
SECRET_KEY = 'django-insecure-gdacrblv!o(4((^6e&2%g+ctkuz$0c1#%z27t9d4dnd-=f=^2m'
DEBUG = True

# 🌐 Allowed Hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

# 🧱 Aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventario',  # Tu app principal
]

# 🛡 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔗 URLs y WSGI
ROOT_URLCONF = 'maestranza_inventario.urls'
WSGI_APPLICATION = 'maestranza_inventario.wsgi.application'

# 🗂 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🧮 Base de Datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 Validadores de Contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 Internacionalización
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 📂 Archivos estáticos y multimedia
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🔒 Login
LOGIN_URL = '/login/'

# 🔧 Configuración por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 📧 Configuración de correo electrónico con sanitización
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'maestranzaduoc@gmail.com'

# 🛡 Limpieza de caracteres no ASCII (como \xa0)
def clean_password(raw_pass):
    try:
        return raw_pass.encode("ascii").decode("ascii")
    except UnicodeEncodeError:
        print("⚠ WARNING: EMAIL_HOST_PASSWORD contiene caracteres inválidos.", file=sys.stderr)
        return raw_pass.replace('\xa0', '').strip()

EMAIL_HOST_PASSWORD = clean_password('tcwb tvky ilel wwkd')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER