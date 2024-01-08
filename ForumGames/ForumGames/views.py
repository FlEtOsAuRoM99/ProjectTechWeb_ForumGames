from django.shortcuts import render, redirect
from Computer.models import ComponentsComputer
from Post.forms import WritePost
from Post.models import Post
def home(request):

    photo = elPC = post = None
    if request.user.is_authenticated:
        components= ComponentsComputer.objects.filter(nickname_id=request.user.id).all()

        if not components.exists():
            return redirect("Computer:createComputer")
        else:
            post_formatting = Post.objects.filter(user_id=request.user.id).all()
            elPC = []
            photo = []
            for i in range(len(components)):
                elPC.append("CPU: " + components[i].CPU)
                elPC.append("GPU: " + components[i].GPU)
                elPC.append("RAM: " + components[i].RAM)
                elPC.append("MEM: " + components[i].MEM)
                elPC.append("PSU: " + components[i].PSU)
                elPC.append("MOBO: " + components[i].MOBO)
                elPC.append(components[i].PC_Photo)    
        post = WritePost(request.POST or None)
    ctx={"elenco": elPC, "ph": photo, "form": post}

    return render(request=request, template_name="html/ForumGames/Blog.html", context=ctx)
                 
     