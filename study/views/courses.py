from django.shortcuts import render
from django.db import models
from study.models import EgitmenModel,DerslerModel


def KurslarView(request):
    ders = DerslerModel.objects.all()
    egitmenler = EgitmenModel.objects.all()
    return render(request,"pages/courses.html",context={
        "ders":ders,
        "egitmenler":egitmenler
    })

