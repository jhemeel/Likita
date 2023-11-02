from django.shortcuts import get_list_or_404
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
import os, environ

from .models import Appointment
from base.models import User


class AppointmentSitemap(Sitemap):
    changefreq = "always"
    priority = 0.85
    protocol = os.environ.get('PROTOCOL')
    
    def items(self):
        return get_list_or_404(Appointment)
    
    
    def lastmod(self, obj):
        return obj.updated_at
    
    
    def location(self, obj):
        return '/booking-submit/'
    
    
class UserPannelSitemap(Sitemap):
    changefreq = "always"
    priority = 0.85
    protocol = os.environ.get('PROTOCOL')
    
    def items(self):
        return get_list_or_404(Appointment, name__is_staff = False)
    
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return '/user-panel/'
    
    
class StaffPannelSitemap(Sitemap):
    changefreq = "always"
    priority = 0.85
    protocol = os.environ.get('PROTOCOL')
    
    def items(self):
        return get_list_or_404(Appointment, name__is_staff = True)
    
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return '/staff-panel/'