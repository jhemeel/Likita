from django.db import models
from django.contrib import admin
from .models import User, Categories, Post, Topic,LikedPost, Comment, CommentReply, HealthTips


from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body', 'overview')
    
    list_display = ['topic', 'headline', 'owner', 'status', 'created_at', 'published_at']
    list_filter = ['status', 'created_at', 'published_at']
    search_fields = ['topic__title', 'headline']
    prepopulated_fields = {'id': ('topic',)}
    ordering = ['status', '-created_at']
    raw_id_fields = ['owner']
    date_hierarchy = 'published_at'


admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Topic)
admin.site.register(LikedPost)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(HealthTips)
