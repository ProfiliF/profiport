import os

# Determinar el archivo de configuración según la variable de entorno
settings_module = os.getenv("DJANGO_SETTINGS_MODULE", "profiport.settings.local")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
