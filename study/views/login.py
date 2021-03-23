from django.shortcuts import render

def Login(request):
    return render(request,"pages/login.html")