from django.contrib.auth.models import User
from django import forms
from .models import textpost, Images

class DateInput(forms.DateInput):
    input_type = 'date'

class PostForm(forms.ModelForm):
        publish = forms.DateField(widget=forms.SelectDateWidget)
        class Meta:
            model = textpost
            fields = ['text_post_title','text_post_content',
                      'comments_select',
                       'draft','publish','pictureupload', ]



class FileFieldForm(forms.Form):
    #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    image = forms.FileField(label='Select a file',)
    class Meta:
        model = Images
