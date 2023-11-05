from django.forms import ModelForm, ClearableFileInput
from base.models import User
from .models import ReplyContact, ContactUs, Subscribe, SendNewsletter
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileForm(ModelForm):
    date_of_birth = forms.DateField(widget = DateInput)
    class Meta:
        model = User
        fields = ['avatar','bio','name','username','date_of_birth','gender','email', 'location','profession']        
        
class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        field = '__all__'  
        exclude = ['id', ]  
        
class ReplyForm(ModelForm):
    class Meta:
        model=ReplyContact
        fields = ['subject','message', 'attachment']
        

class SubscribeForm(ModelForm):
    class Meta:
        model =  Subscribe
        fields = ['email']
        
        
class NewsletterForm(ModelForm):
    class Meta:
        model =  SendNewsletter
        fields = ['letter', 'attachment']
        widgets = {
            'attachment': ClearableFileInput(attrs={"allow_multiple_selected": True}),
        }