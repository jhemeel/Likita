from django.shortcuts import get_list_or_404
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from .models import Post, Comment, CommentReply, LikedPost, HealthTips
import environ, os

class PostModelSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8
    protocol = os.environ.get('PROTOCOL')
    
    def items(self):
        return get_list_or_404(Post, status = Post.Status.PUBLISHED)
    
    
    def lastmod(self, obj):
        return obj.updated_at
    
    
    def location(self, obj):
        return '/blog/)
    
    
class LikedPostModelSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8
    protocol = os.environ.get('PROTOCOL')
    
    def items(self):
        return get_list_or_404(LikedPost)
    
    
    def lastmod(self, obj):
        return obj.updated_at
    
    
    def location(self, obj):
        return '/liked-post/'
         
    
class CommentModelSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8
    protocol = os.environ.get('PROTOCOL')
    
    
    def items(self):
        return get_list_or_404(Comment)
    
    
    def lastmod(self, obj):
        return obj.created_at
    
    
    def location(self, obj):
        return '/post/%s' % (obj.pk)
 
 
class  CommentReplyModelSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8
    protocol = os.environ.get('PROTOCOL')
    
    def items(self):
        return get_list_or_404(CommentReply)
    
    
    def lastmod(self, obj):
        return obj.created_at
    
    
    def location(self, obj):
        return '/post/%s' % (obj.pk)
 

class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = os.environ.get('PROTOCOL')
 
    def items(self):
        
        return ['home', 'login', 'register', 'contact-us' ] #returning static pages; home and contact us
 
    def location(self, item):
        return reverse(item) #returning the static pages URL; home and contact us
