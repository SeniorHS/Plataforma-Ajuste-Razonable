"""
URL configuration for PlataformaAjusteRazonable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Usuario import views as user
from Intranet import views as intra
from Ajustes import views as aju

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.login, name='login'),
    path('registro/', user.registro, name='registro'),
    path('intranet/', intra.intranet, name='noticias'),
    path('ajuste/', aju.ajuste, name='ajuste')

]
