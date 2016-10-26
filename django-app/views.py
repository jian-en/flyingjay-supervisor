from django.conf.urls import url
from django.http import JsonResponse

def json(request):
    return JsonResponse({'message': 'Hello, World!'})

urlpatterns = [
    url('^json', json)
]
