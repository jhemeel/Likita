from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostModelSitemap, CommentModelSitemap,CommentReplyModelSitemap, LikedPostModelSitemap,  StaticSitemap

sitemaps = {
    'post':PostModelSitemap, #add DynamicSitemap to the dictionary
    'comment' : CommentModelSitemap,
    'replies': CommentReplyModelSitemap,
    'liked-post': LikedPostModelSitemap,
    'static':StaticSitemap, #add StaticSitemap to the dictionary
    
}

urlpatterns = [
    

    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    
    path('', views.home, name="home" ),
    path('blog/', views.blog, name='blog'),
    path('create-post/', views.create_post, name="create-post"),
    path('post/<str:pk>/', views.post, name="post"),
    path('post-categories/', views.post_categories, name="post-categories"),
    path('update-post/<str:pk>/', views.update_post, name="update-post"),
    path('liked-post/', views.liked_post, name='liked-post'),
    path('delete-post/<str:pk>/', views.delete_post, name='delete-post'),
    path('replies/<str:pk>/', views.reply_comment, name='replies'),
    path('delete-comment/<str:pk>/', views.delete_comment, name='delete-comment'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('topics/', views.topicsPage, name="topics"),
    
    
]


