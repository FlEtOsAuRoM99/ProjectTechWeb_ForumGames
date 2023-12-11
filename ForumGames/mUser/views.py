from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegUser, logUser
from django.contrib.auth import authenticate
# Create your views here.

def register_req(request):
    form = RegUser(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if form.checkOnlyMail():
                if form.checkPassword():
                    u = User.objects.create_user(form.get_usernameByForm, form.get_emailByForm, form.get_passwordByForm)
                    u.save()
                    return redirect("mUser:Login")
                else:
                    messages.error(request, "Errore nell'inserire la password")
            else:
                messages.error(request, "Mail già in uso")
        else:
            messages.error(request, "Username già in uso")

    return render(request=request,
                  template_name="html/account/register/Register.html",
                  context={"form":form, "error":form.errors})



@login_required
def logout_req(request):
    if request.method == "GET":
        logout(request)
    return redirect("Home")



class Login(LoginView):
    authentication_form = logUser
    form_class = logUser
    template_name="html/account/login/Login.html" 

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        
    def form_valid(self, form):
        login(self.request, form.get_user())
        print(form.errors.as_json())
        return super(LoginView, self).form_valid(form)
    
    def form_invalid(self, form):
        
        messages.error(self.request, "Username o password errate")
        form.errors.pop("__all__")
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self) -> str:
        return super().get_success_url()