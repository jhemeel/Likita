from rest_framework import serializers
from base.models import User, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','avatar', 'name','first_name', 'last_name', 'email', 'location', 'profession']
        
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        