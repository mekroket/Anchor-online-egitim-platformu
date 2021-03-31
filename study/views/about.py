from django.shortcuts import render
from study.models import EgitmenModel
from django.db import models
from django.core.paginator import Paginator
def Hakkımızda(request):
        egitmenler = EgitmenModel.objects.all()
        return render(request,"pages/about.html",context={
            "egitmenler":egitmenler
        })