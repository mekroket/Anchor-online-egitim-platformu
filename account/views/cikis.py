from django.contrib.auth import logout
from django.shortcuts import redirect

def Cikis(request):
    logout(request)
    return redirect("anasayfa")