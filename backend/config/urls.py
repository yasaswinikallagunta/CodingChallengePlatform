from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def root_health_check(request):
    return JsonResponse({
        'status': 'ok',
        'service': 'Coding Challenge Platform API',
        'version': '1.0.0',
        'endpoints': {
            'api': '/api/',
            'auth_register': '/api/auth/register/',
            'auth_login': '/api/auth/login/',
            'problems': '/api/problems/',
            'exams': '/api/exams/',
            'certificates': '/api/certificates/',
        }
    })

urlpatterns = [
    path('', root_health_check, name='root-health'),
    path('health/', root_health_check, name='health-check'),
    path('admin/', admin.site.urls),
    path('api/', include('coding.urls')),
]
