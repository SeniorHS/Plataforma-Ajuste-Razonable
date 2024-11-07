from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login/login.html")

def registro(request):
    return render(request, "registro/registro.html")