from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewPC
# Create your views here.

@login_required
def create(request):
    if request.method == 'POST':
        form = NewPC(request.POST, request.FILES)
        if form.is_valid():
            form.savePC(request)
            return redirect("Home")
        else:
            messages.error(request, "")
    form = NewPC(None)

    return render(request=request,
                  template_name="html/account/register/computer/createComputer.html",
                  context={"form":form, "error":form.errors})
