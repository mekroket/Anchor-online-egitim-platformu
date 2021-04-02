from django.shortcuts import render,get_object_or_404
from django.db import models
from study.models import YazilarModel,EgitmenModel,KategoriModel,DerslerModel,AboutModel
from django.core.paginator import Paginator

def Kategori(request, KategoriSlug):
        kategori = get_object_or_404(KategoriModel , slug=KategoriSlug)
        yazilar = YazilarModel.objects.all()
        return render(request,"pages/index.html",context={
            "yazilar": yazilar,
            "egitmenler":egitmenler,
            "ders":ders,
            "ceo":ceo            
        })