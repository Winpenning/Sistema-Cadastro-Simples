from django.shortcuts import render
from .models import Usuario
# Create your views here.
def home(request):
    return render(request,'home.html')

def usuarios(request):
    novousuario = Usuario()
    novousuario.nome = request.POST.get('nome')
    novousuario.idade = request.POST.get('idade')
    novousuario.save()
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    return render(request,'usuarios.html',usuarios)