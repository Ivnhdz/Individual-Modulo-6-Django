from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import MiFormulario

# Create your views here.

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    users = User.objects.all()
    return render(request, 'usuarios.html', {'users': users})

def crearFormulario(request):
    if request.method == "POST":
        form = MiFormulario(request.POST)
        if form.is_valid():
            Mensaje = form.save(commit=False)
            Mensaje.save()
    formulario_get = MiFormulario()
    return render(request,"formulario.html",{'form':formulario_get})