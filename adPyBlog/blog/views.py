from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def index(request):
    allPosts = Post.objects.all()
    return render(request, "blog/blogHome.html", {"allPosts": allPosts})

def post(request, slug):
    post = Post.objects.filter(slug=slug)
    if len(post) == 0:
        return render(request, "error.html")
    return render(request, "blog/blogPost.html", {"post": post[0]})