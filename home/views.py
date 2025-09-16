from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home/test.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 1 or len(email) < 5 or len(phone) < 10 or len(content) < 10:
            messages.error(request, "Please fill the form correctly!")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your response has been Submitted")
    return render(request, 'home/contact.html')


def search(request):
    query = request.GET.get('query', '')
    if len(query) > 78:
        allposts = Post.objects.none()
    else:
        allposts = Post.objects.filter(title__icontains=query)
        if not allposts.exists():
            allposts = Post.objects.filter(author__icontains=query)
        if not allposts.exists():
            allposts = Post.objects.filter(content__icontains=query)
    if not allposts.exists():
        messages.warning(request, "No search results found. Please refine your query.")
    context = {'allposts': allposts, 'query': query}
    return render(request, 'home/search.html', context)


# ✅ Sign In (Register new user)
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        inputfname = request.POST['inputfname']
        inputlname = request.POST['inputlname']
        inputemail = request.POST['inputemail']
        inputPassword1 = request.POST['inputPassword1']
        inputPassword2 = request.POST['inputPassword2']

        if inputPassword1 != inputPassword2:
            messages.error(request, "Passwords do not match")
            return redirect("home")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("home")

        myuser = User.objects.create_user(username, inputemail, inputPassword1)
        myuser.first_name = inputfname
        myuser.last_name = inputlname
        myuser.save()
        messages.success(request, "Your account has been created Successfully")
        return redirect("home")
    return redirect("home")


# ✅ Login existing user
def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect("home")
    return redirect("home")






def handleLogout(request):
    logout(request)
    return redirect('/')

