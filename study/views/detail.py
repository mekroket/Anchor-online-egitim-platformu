from django.shortcuts import render

def Detail(request,slug):
    return render(request,"pages/detail.html",context={})