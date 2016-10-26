from django.conf import settings

settings.configure(
    ALLOWED_HOSTS = ('127.0.0.1', 'localhost'),
    ROOT_URLCONF='views',
)

from django.core.handlers.wsgi import WSGIHandler
app = WSGIHandler()
