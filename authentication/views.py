from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.contrib import messages
from django.contrib.auth import authenticate,login

def home(request):
    return render(request, "authentication/index.html")

def signin(request):
    return render(request, "authentication/signin.html")

    if request.method == 'POST':
        username = requset.POST['username']
        pass1 = requset.POST['pass1']


        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname':fname})
             

        else:
            messages.error(request, "Bad username or password")
            return redirect('home')

    #     if username == "dmuondu" and pass1 =f= "apple12.":
    #         return "Yay"
            

        

def signout(request):
    pass 