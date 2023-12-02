from django.shortcuts import render

def home(request):
    
    return render(request=request,
                  template_name="html/ForumGames/Blog.html")