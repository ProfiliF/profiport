"""
Production settings for profiport project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from .base import *  # Importar la configuración base
import dj_database_url
import os

# Security settings
SECRET_KEY = os.getenv("SECRET_KEY")  # Se obtiene de una variable de entorno
DEBUG = False  # En producción, siempre debe ser False
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "your-production-domain.com").split(",")  # Lista de dominios permitidos

# Database
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL")  # Heroku configura automáticamente esta variable
    )
}

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Middleware para servir archivos estáticos en producción
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# Security enhancements
SECURE_SSL_REDIRECT = True  # Redirige todo el tráfico HTTP a HTTPS
SECURE_HSTS_SECONDS = 31536000  # HSTS para 1 año
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True  # Solo cookies seguras
SESSION_COOKIE_SECURE = True

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "logs/errors.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
