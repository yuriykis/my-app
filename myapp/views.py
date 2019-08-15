from django.shortcuts import render, get_object_or_404
from .models import Osoba
from .forms import Osoba_add
from django.shortcuts import redirect

# Create your views here.
def base_list(request):
    osoby = Osoba.objects.all()
    return render(request, 'myapp/base_list.html', {'osoby': osoby})

def entity_detail(request, pk):
   osoba = get_object_or_404(Osoba, pk=pk)
   return render(request, 'myapp/entity_detail.html', {'osoba': osoba})

def osoba_new(request):
    if request.method == "POST":
        form = Osoba_add(request.POST)
        if form.is_valid():
            osoba = form.save()
            osoba.save()
            return redirect('base_list')
    else:
        form = Osoba_add()
    return render(request, 'myapp/osoba_edit.html', {'form': form})

def osoba_edit(request, pk):
    osoba = get_object_or_404(Osoba, pk=pk)
    if request.method == "POST":
        form = Osoba_add(request.POST, instance=osoba)
        if form.is_valid():
            osoba = form.save()
            osoba.save()
            return redirect('base_list')
    else:
       form=Osoba_add(instance=osoba)
    return render(request, 'myapp/osoba_edit.html', {'form': form})


def osoba_delete(request, pk):
    osoba = get_object_or_404(Osoba, pk=pk)
    osoba.delete()
    osoby = Osoba.objects.all()
    return redirect('base_list')

