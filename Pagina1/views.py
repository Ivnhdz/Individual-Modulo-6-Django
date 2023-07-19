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
    form = MiFormulario()
    return render(request,"formulario.html",{'form':form})