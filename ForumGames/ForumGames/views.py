from django.shortcuts import render, redirect
from Computer.models import ComponentsComputer
from Post.forms import WritePost
def home(request):

    photo = elPC = post = None
    if request.user.id != None:
        l = ComponentsComputer.objects.filter(nickname_id=request.user.id).all()
        if not l.exists():
            return redirect("Computer:createComputer")
        else:
            elPC = []
            for i in range(len(l)):
                elPC.append("CPU: " + l[i].CPU)
                elPC.append("GPU: " + l[i].GPU)
                elPC.append("RAM: " + l[i].RAM)
                elPC.append("MEM: " + l[i].MEM)
                elPC.append("PSU: " + l[i].PSU)
                elPC.append("MOBO: " + l[i].MOBO)
                photo = l[i].PC_Photo
        post = WritePost(request.POST or None)
    ctx={"elenco": elPC, "ph": photo, "form": post}

    return render(request=request, template_name="html/ForumGames/Blog.html", context=ctx)
                 
     