from django.urls import path
from study.views import KurslarView,trainers,articles,Register,Login,Kurs,Kategori,Hakkımızda,Cash,Detail,KursSayfası
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path("kurslar",KurslarView,name="kurslar"),
    path("alistirma",TemplateView.as_view(template_name="pages/trainers.html"),name="alistirma"),
    path("kayit-ol",TemplateView.as_view(template_name="pages/register.html"),name="kayit-ol"),
    path("giris-yap",TemplateView.as_view(template_name="pages/login.html"),name="giris-yap"),
    path("kurs",TemplateView.as_view(template_name="pages/kurs.html"),name="kurs"),
    path("kategori/<int:id>",Kategori,name="kategori"),
    path("kurs-detay/<int:id>",Detail,name="kurs-detay"),
    path("kurs-icerigi",KursSayfası,name="kurs-icerigi"),
    
] 