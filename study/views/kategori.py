from django.shortcuts import render,get_object_or_404
from django.db import models
from study.models import YazilarModel,KategoriModel
from django.core.paginator import Paginator

def Kategori(request,kategoriSlug):
        kategori = get_object_or_404(KategoriModel , slug=kategoriSlug)
        yazilar = YazilarModel.objects.all()
        return render(request,"pages/index.html",context={
            "yazilar": yazilar,          
        })