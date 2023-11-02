from django.urls import path
from .views import profile, about_me, gallery, contact_me,reply_contacts, subscribe, send_newsletter

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap

sitemaps = {
    'static':StaticSitemap, #add StaticSitemap to the dictionary
    
}

urlpatterns = [
    
    path('profile_sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    path('profile/<str:pk>/', profile, name='profile'),
    path('about-me/', about_me, name='about-me'),
    path('contact/', contact_me, name='contact'),
    path('reply-contact/<str:pk>/', reply_contacts, name='reply-contact'),
    path('subscribe/', subscribe, name='subscribe'),
    path('send-newsletter/', send_newsletter, name='send-newsletter'),
    path('gallery/', gallery, name='gallery'),
]
