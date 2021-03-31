from django.shortcuts import render
from django.db import models
from study.models import YazilarModel
from django.core.paginator import Paginator

def Anasayfa(request):
        yazilar = YazilarModel.objects.all()
        return render(request,"pages/index.html",context={
            "yazilar": yazilar
        })