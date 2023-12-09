
from django import forms
from django.contrib.auth.models import User
import re

class RegUser(forms.ModelForm):  
    username = forms.CharField(label="Enter username", required=True, max_length=30, widget=forms.TextInput())
    email = forms.EmailField(label="Enter email", required=True, max_length=40, widget=forms.EmailInput())
    password = forms.CharField(label="Enter password", required=True, max_length=300, widget=forms.PasswordInput())
    c_password = forms.CharField(label="Enter same password", required=True, max_length=300, widget=forms.PasswordInput())
    
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
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,300}$"
        if self.get_passwordByForm == self.get_c_passwordByForm:
            if len(self.get_passwordByForm) >= 8 and re.search(re.compile(reg), self.get_passwordByForm):
                return True
        return False