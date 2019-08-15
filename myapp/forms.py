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