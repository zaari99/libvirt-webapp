from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.


def accesPage(request):
    #recuperation des donnees
    if request.method == "POST":
        nom=request.POST.get('username')
        passwd=request.POST.get('password')
        user=authenticate(request,username=nom,password=passwd)
        # si l'utilisateur est existe
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"il y a une erreur le comte n'existe pas ")
    context={}
    return render(request,'compte/acces.html')

def logOut(request):
    logout(request)
    return redirect("acces")