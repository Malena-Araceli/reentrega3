from django.shortcuts import render
from Curso.models import camadaCurso
from Curso.forms import cursoFormulario
# Create your views here.
def inicio (request):
    return render(request, "Curso/index.html")

def curso (request):
    return render(request, "Curso/curso.html")

def profesores (request):
    return render(request, "Curso/profesores.html")

def estudiantes (request):
    return render(request, "Curso/estudiantes.html")

def entregables (request):
    return render(request, "Curso/entregables.html")

def entregables (request):
    return render(request, "Curso/entregables.html")


def cursoFormulario(request):
    if request.method == "POST":
        curso = request.POST.get('curso')
        camada = request.POST.get('camada')
        
        nuevo_curso = camadaCurso(nombre=curso, camada=camada)
        nuevo_curso.save()
        
        return render(request, "Curso/index.html")
    
    return render(request, "Curso/cursoFormulario.html")

