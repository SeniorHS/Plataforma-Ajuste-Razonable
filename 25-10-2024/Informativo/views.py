from django.shortcuts import render

# Create your views here.

def informativo(request):
    return render(request, 'informativo/informativo.html')
