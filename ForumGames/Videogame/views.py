from django.shortcuts import render, redirect
from .forms import addFormVideogame
from .models import PossVideogames
# Create your views here.

def addVideogame(request):
    print("o")
    form = addFormVideogame(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.saveVideogame(request)
            return redirect('Home')
        else:
            pass

    return render(request=request,
                  template_name="html/account/register/videogame/addVideogame.html",
                  context={"form":form})
