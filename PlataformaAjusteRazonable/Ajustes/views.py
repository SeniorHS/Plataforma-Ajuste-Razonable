from django.shortcuts import render

# Create your views here.

def ajuste(request):
    return render(request, 'ajuste/ajuste.html')