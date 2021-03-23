from django.shortcuts import render

def Makaleler(request):
    return render(request,"pages/articles.html")