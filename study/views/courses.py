from django.shortcuts import render

def Kurslar(request):
    return render(request,"pages/courses.html")