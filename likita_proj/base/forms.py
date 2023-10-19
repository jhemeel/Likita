from django.forms import ModelForm
from .models import Post, User, CommentReply
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class PostForm(ModelForm):
    overview = SummernoteTextField()
    body = SummernoteTextFormField()
    
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['id', 'owner', 'no_of_liked_post']
        widgets = {
            'overview': SummernoteWidget(),
            'body': SummernoteInplaceWidget(),
        }
        
class ReplyForm(ModelForm):
    
    class Meta:
        model = CommentReply
        fields = ['body']
    