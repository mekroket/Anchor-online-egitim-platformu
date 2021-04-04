from django.shortcuts import render,get_object_or_404
from django.db import models
from study.models import EgitmenModel,DerslerModel


def Detail(request,id):
    ders = get_object_or_404(DerslerModel,id=id)
    return render(request,"pages/detail.html",context={
        "ders":ders,
    })