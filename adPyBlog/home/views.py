from turtle import title
from django.shortcuts import render, HttpResponse
from django.contrib import messages # type: ignore
from home.models import Contact
from blog.models import Post

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    
    if request.method == "POST":
        frs = request.POST.get('frs')
        lst = request.POST.get('lst')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if len(frs)>2 and len(lst)>1 and len(email)>4 and len(phone)>9 and len(desc)>4:
            contactdata = Contact(first_name=frs, last_name=lst, email=email, phone=phone, content=desc)
            contactdata.save()
            return render(request, "home/contactSubmit.html")
        else:
            messages.error(request, "Please fill the form correctly")
       
    return render(request, 'home/contact.html')


def test(request):
    return render(request, "home/contactSubmit.html")

def search(request):
    q = request.GET.get("q")
    if q == None:
        return render(request, "error.html")
    allposts = Post.objects.filter(title__icontains=q)

    params = {
        "posts": allposts,
        "length": len(allposts),
        "q":q
    }
    return render(request, "home/search.html", params)