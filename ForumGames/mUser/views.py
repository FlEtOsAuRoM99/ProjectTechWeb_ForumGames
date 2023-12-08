from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegUser
# Create your views here.

def register_req(request):
    form = RegUser(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if form.checkOnlyMail():
                u = User.objects.create_user(form.get_usernameByForm, form.get_emailByForm, form.get_passwordByForm)
                u.save()
                return redirect("mUser:Login")
            else:
                messages.error(request, "Mail già in uso")
                print("Mail già in uso")
        else:
            messages.error(request, "Username non valido")

    return render(request=request,
                  template_name="html/account/register/Register.html",
                  context={"form":form, "error":form.errors})

@login_required
def logout_req(request):
    if request.method == "GET":
        logout(request)
    return redirect("Home")

