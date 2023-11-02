from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone
from django_quill.fields import QuillField

# Create your models here.


class User(AbstractUser):
    
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEAMLE = "F", "Female"
        NIL = "", "Prefer not to say"
        
    email = models.EmailField(unique=True, help_text="Enter active email address")
    name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(default="1990-05-25")
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE)
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=150)
    class Meta:
        verbose_name_plural = 'Category'    
        
    def __str__(self):
        return self.title
    
           

class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    
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
    categories =models.ManyToManyField(Categories, related_name='post_categories')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    overview =  QuillField()
    body = QuillField()
    status = models.CharField(choices = Status.choices,  default=Status.DRAFT, max_length=2)
    image = models.ImageField(upload_to="post-media")
    no_of_liked_post = models.IntegerField(default=0)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Post'
        ordering = [ '-updated_at', "-created_at"]
        
        indexes = [
            models.Index(fields=['-created_at', '-updated_at']),
        ]
        
    def __str__(self):
        return self.headline    
 
    
class LikedPost(models.Model):
    post_id = models.CharField(max_length=500)
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(default = timezone.now)
    
    class Meta:
        verbose_name_plural = 'LikedPost'
    
    def __str__(self):
        return self.user


class Comment(models.Model):
    id = models.UUIDField( primary_key=True, default=uuid.uuid4 )
    sender  = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
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
        return f'{self.replier.username} : {self.replier}'
    

class HealthTips(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = QuillField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "HealthTip"
        
    def __str__(self):
        return self.content
    
        
   
    