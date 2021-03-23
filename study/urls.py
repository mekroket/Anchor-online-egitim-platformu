from django.urls import path
from study.views import index,about,Kurslar,trainers,articles,Register,Login
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path("",index,name="index"),
    path("about",TemplateView.as_view(template_name="pages/about.html"),name="about"),
    path("kurslar",TemplateView.as_view(template_name="pages/courses.html"),name="kurslar"),
    path("alistirma",TemplateView.as_view(template_name="pages/trainers.html"),name="alistirma"),
    path("makaleler",TemplateView.as_view(template_name="pages/articles.html"),name="makaleler"),
    path("ödeme",TemplateView.as_view(template_name="pages/cash.html"),name="ödeme"),
    path("iletisim",TemplateView.as_view(template_name="pages/contact.html"),name="iletisim"),
    path("kayit-ol",TemplateView.as_view(template_name="pages/register.html"),name="kayit-ol"),
    path("giris-yap",TemplateView.as_view(template_name="pages/login.html"),name="giris-yap"),
] 