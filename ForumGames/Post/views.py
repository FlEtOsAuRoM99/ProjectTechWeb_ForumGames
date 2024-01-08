from django.shortcuts import render, redirect
from .forms import WritePost

# Create your views here.

def postInsert(request):
    print("ciao")
    if request.method == 'POST':
        form = WritePost(request.POST)
        form.savePost(request)
    else:
        form = WritePost()

    return render(request=request,
                  template_name="html/ForumGames/Blog.html",
                  context={"form":form})