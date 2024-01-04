from django.shortcuts import render

# Create your views here.

def addVideogame(request):
    

    return render(request=request,
                  template_name="html/account/register/videogame/addVideogame.html",
                  context={"form":form})
