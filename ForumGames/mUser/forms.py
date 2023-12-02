
from django import forms
from django.contrib.auth.models import User


class RegUser(forms.ModelForm):  
    username = forms.CharField(label="Enter username", required=True, max_length=30, widget=forms.TextInput())
    email = forms.EmailField(label="Enter email", required=True, max_length=40, widget=forms.EmailInput())
    password = forms.CharField(label="Enter password", required=True, max_length=300, widget=forms.PasswordInput())
   
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
    
    def checkOnlyMail(self):
        if User.objects.filter(email=self.get_emailByForm).exists():
            return False
        return True