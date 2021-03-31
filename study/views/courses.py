from django.shortcuts import render
from study.models import KurslarGörüntüle

#! burda indexe değer dönmüyor düzeltilecek
def Kurslar(request):
        dersler = KurslarGörüntüle.objects.all()
        return render(request,"pages/courses.html",context={
            "dersler":dersler,
        })