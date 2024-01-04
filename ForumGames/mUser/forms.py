
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
import re

class RegUser(forms.ModelForm):  
    username = forms.CharField(label="", required=True, max_length=30, widget=forms.TextInput(attrs={"placeholder": "Inserire username"}))
    email = forms.EmailField(label="", required=True, max_length=40, widget=forms.EmailInput(attrs={"placeholder": "Inserire email"}))
    password = forms.CharField(label="", required=True, max_length=300, widget=forms.PasswordInput(attrs={"placeholder": "Inserire password"}))
    c_password = forms.CharField(label="", required=True, max_length=300, widget=forms.PasswordInput(attrs={"placeholder": "Inserire la stessa password"}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    class Meta:
        model = User
        fields = ["username", "email", "password"]
    
    @property  
    def get_usernameByForm(self):
        return self.cleaned_data["username"]
    
    @property  
    def get_emailByForm(self):
        return self.cleaned_data["email"]
    @property  
    def get_passwordByForm(self):
        return self.cleaned_data["password"]
    
    @property
    def get_c_passwordByForm(self):
        return self.cleaned_data["c_password"]


    def checkOnlyMail(self):
        if User.objects.filter(email=self.get_emailByForm).exists():
            return False
        return True

    def checkPassword(self):
        
        if self.get_passwordByForm == self.get_c_passwordByForm:
            capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            smallalphabets="abcdefghijklmnopqrstuvwxyz"
            specialchar="$@#\'\\<>{ }-àùè.:,;+*/[]()£\"!&%?ì^=_"
            digits="0123456789"
            if (len(self.get_passwordByForm) >= 8):
                l = u = d = p = 0
                for i in self.get_passwordByForm:
            
                    # counting lowercase alphabets
                    if (i in smallalphabets):
                        l+=1           
            
                    # counting uppercase alphabets
                    if (i in capitalalphabets):
                        u+=1           
            
                    # counting digits
                    if (i in digits):
                        d+=1           
            
                    # counting the mentioned special characters
                    if(i in specialchar):
                        p+=1       
            if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(self.get_passwordByForm)):
                return True
        
        return False
    

class logUser(AuthenticationForm):
    
    username = forms.CharField(label="", required=True, max_length=30, widget=forms.TextInput(attrs={"placeholder":"Inserire username"}))
    password = forms.CharField(label="", required=True, max_length=300, widget=forms.PasswordInput(attrs={"placeholder":"Inserire password"}))
    
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
