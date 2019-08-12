from django.shortcuts import render

# Create your views here.
def base_list(request):
    return render(request, 'myapp/base_list.html')
