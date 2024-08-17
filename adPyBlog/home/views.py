
from django.shortcuts import render, redirect
from django.contrib import messages # type: ignore
from home.models import Contact
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login 

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
    return render(request, "home/login.html")

def search(request):
    q = request.GET.get("q")
    if q == None:
        return render(request, "error.html")
    if len(q) > 78:
        allposts =[]
    else:
        allpostsTitle = Post.objects.filter(title__icontains=q)
        allpostsContent = Post.objects.filter(content__icontains=q)
        allposts = allpostsTitle.union(allpostsContent)

    params = {
        "posts": allposts,
        "length": len(allposts),
        "q":q
    }
    return render(request, "home/search.html", params)

def handelLogin(request):
    if request.user.username != "":
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            messages.error(request, "Incorrect username or password")
            return render(request, "home/login.html")
        
        login(request, user)
        return redirect("/")
           
    return render(request, "home/login.html")

def signup(request):
    if request.user.username != "":
        return redirect("/")
    if request.method == "POST":
        frs = request.POST.get('frs')
        lst = request.POST.get('lst')
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if len(frs) < 2:
            messages.error(request, "First name is too short")
            return render(request, "home/signup.html")
        
        if len(lst) < 2:
            messages.error(request, "Last name is too short")
            return render(request, "home/signup.html")
        
        if len(email) < 4:
            messages.error(request, "Email is too short")
            return render(request, "home/signup.html")
        
        if len(username) < 2:
            messages.error(request, "Username is too short")
            return render(request, "home/signup.html")
        
        specialChars = ["~", "`", "=", "+", ";", ":", "!", "#", "$", "@", "%", "^", "&", "*", "(", ")", "{","}","|", chr(92), "'", '"', ",","<",">",".","/","?"]
        
        for char in username:
            if char in specialChars:
                messages.error(request, "Username not contains any special cherecter excape '-' and '_'")
                return render(request, "home/signup.html")
        
        if len(password) < 7:
            messages.error(request, "Pasword is too short")
            return render(request, "home/signup.html")
        
        existUsername = User.objects.filter(username=username)
        existEmail = User.objects.filter(email=email)

        if len(existUsername) != 0 :
            messages.error(request, "Username is already taken")
            return render(request, "home/signup.html")
        
        if len(existEmail) != 0:
            messages.error(request, "Email is already taken")
            return render(request, "home/signup.html")
        
        user = User.objects.create_user(username, email, password)
        user.first_name = frs
        user.last_name = lst
        user.save()
        return redirect("/login")
        
    return render(request, "home/signup.html")

def handelLogout(request):
    logout(request)
    return redirect("/")
