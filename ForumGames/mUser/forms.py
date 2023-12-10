
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
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,300}$"
        if self.get_passwordByForm == self.get_c_passwordByForm:
            if len(self.get_passwordByForm) >= 8 and re.search(re.compile(reg), self.get_passwordByForm):
                return True
        return False
    

class logUser(AuthenticationForm):
    
    username = forms.CharField(label="", required=True, max_length=30, widget=forms.TextInput(attrs={"placeholder":"Inserire username"}))
    password = forms.CharField(label="", required=True, max_length=300, widget=forms.PasswordInput(attrs={"placeholder":"Inserire password"}))
    
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password'].help_text = None
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    class Meta:
        model = User
        fields = ["username","password"]

        labels={
            "username": "",
            "password": "",
        }
        
        help_texts = {
            'username': None,
            'password': None,
        }

        widgets={
            "username": forms.TextInput(attrs={"placeholder":"Inserire username"}),
            "password": forms.PasswordInput(attrs={"placeholder":"Inserire password"}),
        }
        '''