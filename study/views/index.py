from django.shortcuts import render
from django.db import models
from study.models import YazilarModel,EgitmenModel
from django.core.paginator import Paginator

def Anasayfa(request):
        yazilar = YazilarModel.objects.all()
        egitmenler = EgitmenModel.objects.all()
        return render(request,"pages/index.html",context={
            "yazilar": yazilar,
            "egitmenler":egitmenler,
        })