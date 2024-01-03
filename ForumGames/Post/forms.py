
from django import forms
from django.contrib.auth.models import User
from .models import Post
import re

class WritePost(forms.ModelForm):  

    title = forms.CharField(label="Enter title")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    class Meta: 
        model = Post
        exlude =  ["P_ID_num", "user_id"]
    


