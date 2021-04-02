from django.urls import path
from study.views import Anasayfa,about,KurslarView,trainers,articles,Register,Login,Kurs,Kategori,Hakkımızda,Cash
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path("",Anasayfa,name="anasayfa"),
    path("about",Hakkımızda,name="about"),
    path("kurslar",KurslarView,name="kurslar"),
    path("alistirma",TemplateView.as_view(template_name="pages/trainers.html"),name="alistirma"),
    path("makaleler",TemplateView.as_view(template_name="pages/articles.html"),name="makaleler"),
    path("ödeme",Cash,name="ödeme"),
    path("iletisim",TemplateView.as_view(template_name="pages/contact.html"),name="iletisim"),
    path("kayit-ol",TemplateView.as_view(template_name="pages/register.html"),name="kayit-ol"),
    path("giris-yap",TemplateView.as_view(template_name="pages/login.html"),name="giris-yap"),
    path("kurs",TemplateView.as_view(template_name="pages/kurs.html"),name="kurs"),
    path("kategori/<slug:kategoriSlug>",Kategori,name="kategori"),
] 