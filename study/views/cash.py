from django.shortcuts import render
from study.models import FiyatlarModel


def Cash(request):
    ödeme = FiyatlarModel.objects.all()
    return render(request,"pages/cash.html",context={
        "ödeme":ödeme
    })