from django.shortcuts import render

# Create your views here.
def intranet(request):
    return render(request,"intranet/intranet.html")