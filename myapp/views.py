from django.shortcuts import render, get_object_or_404
from .models import Osoba
from .forms import Osoba_add, Telefon_add, Email_add, Find_person
from django.shortcuts import redirect
from django.views import generic

# Create your views here.

class BaseView(generic.ListView):
    template_name = 'myapp/base_list.html'
    context_object_name = 'osoby'
    def get_queryset(self):
        return Osoba.objects.all()

def base_list(request):
    osoby = Osoba.objects.all()
    return render(request, 'myapp/base_list.html', {'osoby': osoby})

def entity_detail(request, pk):
   osoba = get_object_or_404(Osoba, pk=pk)
   return render(request, 'myapp/entity_detail.html', {'osoba': osoba})

def osoba_new(request):
    if request.method == "POST":
        form_o = Osoba_add(request.POST)
        if form_o.is_valid():
            osoba = form_o.save()
            osoba.save()
            return redirect('base_list')
    else:
        form_o = Osoba_add()
    return render(request, 'myapp/osoba_edit.html', {'form_o': form_o})

def add_os_tel(request, pk):
    osoba = get_object_or_404(Osoba, pk=pk)
    if request.method == "POST":
        form_t = Telefon_add(request.POST)
        if form_t.is_valid():
            telefon = form_t.cleaned_data['telefon']
            osoba.telefon_set.create(telefon = telefon)
            return redirect('base_list')
    else:
        osoba = get_object_or_404(Osoba, pk=pk)
        form_t = Telefon_add()
    return render(request, 'myapp/add_os_tel.html', {'form_t': form_t,'osoba': osoba})

def add_os_mail(request, pk):
    osoba = get_object_or_404(Osoba, pk=pk)
    if request.method == "POST":
        form_m = Email_add(request.POST)
        if form_m.is_valid():
            mail = form_m.cleaned_data['email']
            osoba.email_set.create(email = mail)
            return redirect('base_list')
    else:
        osoba = get_object_or_404(Osoba, pk=pk)
        form_m = Email_add()
    return render(request, 'myapp/add_os_mail.html', {'form_m': form_m, 'osoba': osoba})

def osoba_edit(request, pk):
    osoba = get_object_or_404(Osoba, pk=pk)
    if request.method == "POST":
        form_o = Osoba_add(request.POST, instance=osoba)
        if form_o.is_valid():
            osoba = form_o.save()
            osoba.save()
            return redirect('base_list')
    else:
       form_o=Osoba_add(instance=osoba)
    return render(request, 'myapp/osoba_edit.html', {'form_o': form_o})


def osoba_delete(request, pk):
    osoba = get_object_or_404(Osoba, pk=pk)
    if osoba.telefon_set.exists() or osoba.email_set.exists():
        return render(request, 'myapp/delete_error.html', {'osoba': osoba})
    else:
        osoba.delete()
    return redirect('base_list')

def osoba_szukaj(request):
    if request.method == "POST":
        form_f = Find_person(request.POST)
        all_persons = Osoba.objects.all()

        if form_f['imie'].value():
            imie = form_f['imie'].value()
            all_persons = all_persons.filter(imie = imie)
        if form_f['nazwisko'].value():
            nazwisko = form_f['nazwisko'].value()
            all_persons = all_persons.filter(nazwisko = nazwisko)
        if form_f['telefon'].value():
           telefon = form_f['telefon'].value()
           all_persons = all_persons.filter(telefon__telefon=telefon)
        if form_f['email'].value():
           email = form_f['email'].value()
           all_persons = all_persons.filter(email__email=email)
        
        return render(request, 'myapp/base_list.html', {'osoby': all_persons})

    else:
        form_f = Find_person()
        return render(request, 'myapp/find_person.html', {'form_f': form_f})

