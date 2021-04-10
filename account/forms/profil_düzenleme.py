from django.contrib.auth.forms import UserChangeForm
from account.models import CustomUserModel
from django import forms

class ProfilDuzenlemeForm(UserChangeForm):

    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class":"change-input change-email","placeholder":"Email"}
    ),required=True,max_length=50,label="Email")

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "change-input change-name","placeholder":"Adınız"}
    ),required=True,max_length=50,label="Adınız")

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "change-input change-lastname","placeholder":"Soy Adınız"}
    ),required=True,max_length=50,label="Soy Adınız")
    
    password = None
    class Meta:
        model = CustomUserModel
        fields = ('email', 'first_name', 'last_name', 'avatar')