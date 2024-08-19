from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from blog.models import Post,BlogComment

# Create your views here.
def index(request):
    allPosts = Post.objects.all().order_by("-time_stamp")
    return render(request, "blog/blogHome.html", {"allPosts": allPosts})

def post(request, slug):
    post = Post.objects.filter(slug=slug)
    if len(post) == 0:
        return render(request, "error.html")
    comments = BlogComment.objects.filter(post=post[0], parent=None).order_by("-time_stamp")
    replies = BlogComment.objects.filter(post=post[0]).exclude(parent=None).order_by("-time_stamp")
    
    repDict = {}
    for reply in replies:
        if reply.parent.id in repDict.keys(): # type: ignore
            repDict[reply.parent.id].append(reply) # type: ignore
            
        else:
            repDict[reply.parent.id] = [reply] # type: ignore
            
  
    params = {
        "post": post[0],
        "comments": comments,
        "replies": repDict    
    }
    return render(request, "blog/blogPost.html", params)

def handleComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        postId = request.POST.get("postId")
        post = Post.objects.get(id=postId)
        user = request.user
        commentId = request.POST.get("commentId")
        
        if user.username == "":
            return render(request, 'error.html')
        if len(comment) == 0:
            messages.error(request, "Comment is too short")
            return redirect(f"/blog/{post.slug}")
        if len(postId) == 0:
            return render(request, 'error.html')

        if commentId is not None:
            parentComment = BlogComment.objects.get(id=commentId)
            comment = BlogComment(comment=comment,user=user,post=post,parent=parentComment)
            comment.save()
            messages.success(request, "Reply posted successfully")
        else:
            comment = BlogComment(comment=comment,user=user,post=post,)
            comment.save()
            messages.success(request, "Comment posted successfully")
        return redirect(f"/blog/{post.slug}")
        
    return render(request, "error.html")