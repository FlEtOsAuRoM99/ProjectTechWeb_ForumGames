
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Accounts

class NewUserForm(UserCreationForm):
    nickname = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Accounts
        fields = ["nickname", "mail", "name", "surname", "password1", "password2", "gender", "bornDate", "descr"]

    def save(self, commit=True):
        print("hello")
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class newuser(forms.Form):
    nickname = forms.CharField(required=True, max_length=100)
    mail = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    descr = forms.CharField(widget=forms.Textarea)    

    def reg(self):
        nickname = self.cleaned_data
        print("fatto")
        nickname = nickname.get('nickname')
        print(nickname)
        return nickname