from django.db import models
from django.utils import timezone

class Osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    def __str__(self):
        return self.imie + " " + self.nazwisko

 

class Telefon(models.Model):
    osoba = models.ForeignKey(Osoba, editable=False, on_delete=models.PROTECT)
    telefon = models.CharField(max_length=50)
    def __str__(self):
        return self.telefon
 

class Email(models.Model):
    osoba = models.ForeignKey(Osoba, editable=False, on_delete=models.PROTECT)
    email = models.EmailField()
    def __str__(self):
        return self.email
