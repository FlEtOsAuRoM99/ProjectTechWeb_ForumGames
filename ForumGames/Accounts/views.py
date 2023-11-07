from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, authenticate
from django.contrib import messages
from .models import Accounts
import bcrypt

# Create your views here.
def login(request):
        used = "/register"
        if request.method == 'POST':
            print("Enter: ", Accounts.password)
            '''
            if form.is_valid():
                nickname = form.cleaned_data.get('nickname')
                password = form.cleaned_data.get('password')
                print(nickname)
                user = authenticate(username=nickname, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {nickname}")
                    return redirect('/')
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
            '''
        return render(request = request, 
                      template_name = "html/Login.html", 
                      context={"use": used})
                  
def login_request(request, validation=False):
        form = AuthenticationForm()
        
        return render(request = request, 
                      template_name = "html/Home.html", 
                      context={"form":form})
                  
def register(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        hashPass = bcrypt.hashpw(request.POST.get('password').encode('utf-8'), bcrypt.gensalt())
        mail = request.POST.get('mail')
        descr = request.POST.get('descr')

        if nickname != "" and hashPass != "" and mail != "":
            if len(Accounts.objects.filter(nickname=nickname)) == 1:
                print("nickname unsable")
                messages.error(request, "Hi")
            elif len(Accounts.objects.filter(mail=mail)) == 1:
                print("mail unsable")
            else:
                Accounts(nickname=nickname, mail=mail, password=hashPass, descr=descr).save()
                login(request)
                return redirect("Accounts:Home")
        else:
            print("Before, you must insert all fields")
    used = "/login"
    return render(request = request, 
                  template_name='html/Register.html', 
                  context={"use":used})

def home(request):
    return render(request = request, 
                    template_name = "html/Home.html", 
                    context={"form":Accounts.objects.all})