from django.shortcuts import redirect,render

def Profile(request):
    return render(request,"pages/profile.html")