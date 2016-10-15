from django.contrib.auth.models import User
from django import forms
from .models import Profile, ProfilePictures
from django.db import models




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("website","bio", "phone", "city","organization","work",)
class ProfilePicturesForm(forms.ModelForm):
    pictures = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
            model=ProfilePictures
            fields = ['pictures']
