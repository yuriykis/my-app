from django import forms
from .models import Osoba, Telefon, Email

class Osoba_add(forms.ModelForm):

    class Meta:
        model = Osoba
        fields = ('imie', 'nazwisko',)

class Telefon_add(forms.ModelForm):

    class Meta:
        model = Telefon
        fields = ('telefon',)

class Email_add(forms.ModelForm):

    class Meta:
        model = Email
        fields = ('email',)

class Find_person(forms.Form):
    imie = forms.CharField(required=False)
    nazwisko = forms.CharField(required=False)
    telefon = forms.IntegerField(required=False)
    email = forms.CharField(required=False)
