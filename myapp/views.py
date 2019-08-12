from django.shortcuts import render
from .models import Osoba

# Create your views here.
def base_list(request):
    osoby = Osoba.objects.all()
    return render(request, 'myapp/base_list.html', {'osoby': osoby})
