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
            return redirect('entity_detail', pk=osoba.pk)
    else:
        form = Osoba_add()
    return render(request, 'myapp/osoba_edit.html', {'form': form})