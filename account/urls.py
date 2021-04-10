from django.urls import path
from account.views import Cikis,Sifre_degistir,kayit,Profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("cikis",Cikis,name="cikis"),
    path("sifre-degistir",Sifre_degistir,name="sifre-degistir"),
    path("kayit",kayit,name="kayit"),
    
    path("giris",auth_views.LoginView.as_view(
        template_name="pages/login.html"
    ),name="giris"),
    path("profil-sayfasi",Profile,name="profil-sayfasi"),
]
