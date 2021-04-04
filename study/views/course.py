from django.shortcuts import render

def KursSayfası(request):
    return render(request,"pages/course.html")