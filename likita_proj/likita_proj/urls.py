from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('authy.urls')),
    path('', include('profiles.urls')),
    path('', include('chat.urls')),
    path('', include('clinic.urls')),
    path('api/', include('liki_api.urls')),
    
    path('api-auth/', include('rest_framework.urls')),
    path('verification/', include('verify_email.urls')),
    
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

handler404 = 'base.views.custom_404'