from django.db import models
from django.contrib import admin
from .models import User, Categories, Post, Topic,LikedPost, Comment, CommentReply

from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
# Register your models here.



class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

admin.site.register(User)
admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Categories)
admin.site.register(Topic)
admin.site.register(LikedPost)
admin.site.register(Comment)
admin.site.register(CommentReply)