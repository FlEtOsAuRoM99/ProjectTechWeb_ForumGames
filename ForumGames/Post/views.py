from django.shortcuts import render, redirect
from .forms import WritePost
# Create your views here.

def postInsert(request):
    form = WritePost(request.POST or None)

    return render(request=request,
                  template_name="html/ForumGames/Blog.html",
                  context={"form":form})