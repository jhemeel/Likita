from django import forms
from .models import Post, User, CommentReply
from .models import Categories

class PostForm(forms.ModelForm):
    categories =forms.ModelMultipleChoiceField( queryset=Categories.objects.all(), 
                                               widget=forms.CheckboxSelectMultiple, label = Categories )
    
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['id', 'owner', 'no_of_liked_post']
        
class ReplyForm(forms.ModelForm):
    
    class Meta:
        model = CommentReply
        fields = ['body']
    