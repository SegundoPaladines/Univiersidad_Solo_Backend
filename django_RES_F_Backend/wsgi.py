import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_RES_F_Backend.settings')

application = get_wsgi_application()
