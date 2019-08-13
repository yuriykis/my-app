from django.shortcuts import render, get_object_or_404
from .models import Osoba

# Create your views here.
def base_list(request):
    osoby = Osoba.objects.all()
    return render(request, 'myapp/base_list.html', {'osoby': osoby})

def entity_detail(request, pk):
   osoba = get_object_or_404(Osoba, pk=pk)
   return render(request, 'myapp/entity_detail.html', {'osoba': osoba})