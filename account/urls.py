from django.urls import path
from account.views import Cikis,Sifre_degistir,kayit


urlpatterns = [
    path("cikis",Cikis,name="cikis"),
    path("sifre-degistir",Sifre_degistir,name="sifre-degistir"),
    path("kayit",kayit,name="kayit"),
]
