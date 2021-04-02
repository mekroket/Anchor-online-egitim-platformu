from django.shortcuts import render
from study.models import AboutModel
from django.db import models
from django.core.paginator import Paginator

def Hakkımızda(request):
        ceo = AboutModel.objects.all()
        return render(request,"pages/about.html",context={
            "ceo": ceo
        })