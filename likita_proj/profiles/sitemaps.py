from django.shortcuts import get_list_or_404
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
import os, environ


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = os.environ.get('PROTOCOL')
 
    def items(self):
        
        return ['about-me', 'subscribe', 'contact', 'send-newsletter', ] #returning static pages; home and contact us
 
    def location(self, item):
        return reverse(item) #returning the static pages URL; home and contact us