from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUserModel
from django import forms
from django.contrib.auth.models import User

class KayitFormu(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class":"form-control","placeholder":"Kullanıcı Adı"}
    ),required=True,max_length=50,label="Kullanıcı Adı")

    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class":"form-control","placeholder":"Email"}
    ),required=True,max_length=50,label="Email")

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control","placeholder":"Adınız"}
    ),required=True,max_length=50,label="Adınız")

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control","placeholder":"Soy Adınız"}
    ),required=True,max_length=50,label="Soy Adınız")

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class":"form-control","placeholder":"Şifre"}
    ),required=True,max_length=50,label="Şifreniz")

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class":"form-control","placeholder":"Şifre Doğrula"}
    ),required=True,max_length=50,label="Şifre Doğrula")

    class Meta:
        model =CustomUserModel
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )