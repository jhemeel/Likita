from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    
    age = models.IntegerField(default=18, null=True, blank=True)
    date_of_birth = models.DateField(default="1990-05-25")
    
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"), 
        ("None", "I prefer Not To Say")
        )
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES, null=True, blank=True, default="M")
    profession = models.CharField(max_length=100, null=True, blank=True)
    
    location = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to='profile-image', default='empty-profile.png')
    bio = models.TextField(null=True, blank=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'User'
        
    def __str__(self):
        return self.username

class Categories(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField()
    

    class Meta:
        verbose_name_plural = 'Category'
        
    def __str__(self):
        return self.title
    
           

class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Topic'
    
    def __str__(self):
        return self.title


class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    overview =  MarkdownxField(null = True, blank=True)
    heading = models.CharField(max_length=200, null=True, blank=True)
    body = MarkdownxField(null = True, blank=True)
    Categories =models.ManyToManyField(Categories, related_name='post_categories',)
    status = models.CharField(choices = Status.choices,  default=Status.DRAFT, max_length=2)
    image = models.ImageField(upload_to="post-media")
    no_of_liked_post = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Post'
        ordering = ['-created_at', '-updated_at']
        
        
    def formatted_markdown(self):
        return markdownify(self.body)
        
    def __str__(self):
        return self.heading    
 
    
class LikedPost(models.Model):
    post_id = models.CharField(max_length=500)
    user = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'LikedPost'
    
    def __str__(self):
        return self.user


class Comment(models.Model):
    id = models.UUIDField( primary_key=True, default=uuid.uuid4 )
    sender  = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Comment'
        ordering = ['-created_at', '-updated_at']
        
    
    def __str__(self):
        return f'{self.sender} : {self.body[:20]}'

    
class CommentReply(models.Model):
    id = models.UUIDField( primary_key=True, default=uuid.uuid4 )
    replier = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'CommentReply'
        ordering = ['-created_at', '-updated_at']
        
    
    def __str__(self):
        return f'{self.replier.username} : {self.body[:20]}'
    
