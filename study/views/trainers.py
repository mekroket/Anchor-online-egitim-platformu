from django.shortcuts import render

def trainers(request):
    return render(request,"pages/trainers.html")