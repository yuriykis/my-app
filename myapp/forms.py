from django import forms
from .models import Osoba

class Osoba_add(forms.ModelForm):

    class Meta:
        model = Osoba
        fields = ('imie', 'nazwisko',)

