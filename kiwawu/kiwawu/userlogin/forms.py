from django.contrib.auth.models import User
from django import forms
#from .models import textpost




class userform(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)
        first_name = forms.CharField(required=True)
        last_name = forms.CharField(required=True)
        email = forms.EmailField(required=True)
        class Meta:
            model = User
            fields = ['first_name', 'last_name', 'email', 'username', 'password' ]
