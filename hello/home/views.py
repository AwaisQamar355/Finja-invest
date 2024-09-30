from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib.auth import authenticate , login , logout
from home.models import Home
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    HttpResponse("Hello Welcome to your home page")
    if request.method == "POST":
        email = request.POST.get("email")
        home = Home(email=email , date=datetime.today())
        home.save()
    return render(request,'home.html')
def product(request):
    HttpResponse("Hello Welcome to your home page")
    
    return render(request,'product.html')
def portfolio(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'portfolio.html')
def fmcg(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'fmcg.html')
def agriculture(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'agriculture.html')
def store(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'store.html')
def security(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'security.html')
def license(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'license.html')
def shariah(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'shariah.html')
def faqs(request):
    HttpResponse("Hello Welcome to your home page")
    return render(request,'faqs.html')
def loginuser(request):
    HttpResponse("Hello Welcome to your home page")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("home.html")
        else:
            return redirect("signup.html")
    return render(request,'login.html')
def logoutuser(request):
    HttpResponse("Hello Welcome to your home page")
    logout(request)
    if request.user.is_anonymous:
        return redirect("login.html")
    return render(request,'logout.html')
def signup(request):
    HttpResponse("Hello Welcome to your home page")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeatpassword = request.POST.get("repeatpassword")
        
        # sign = SignUp(username=username , email = email , password =  password , repeatpassword = repeatpassword ,date = datetime.today())
        # sign.save()

        if User.objects.filter(username = username).exists():
            error_message = 'Username already taken. Please choose a different username.'
            return render(request , 'signup.html' ,{'error_message' : error_message})
        
        if password != repeatpassword:
            return HttpResponse("Your Password and confirm password are not the same!")
        
        else:
            myuser = User.objects.create_user(username,email,password)
            myuser.save()
        return redirect('login.html')
    return render(request,'signup.html')









