from django.shortcuts import render
from .models import Service

# Creando vistas de servicios
def services(request):
    services=Service.objects.all()
    return render(request,"services/services.html",{'services':services})