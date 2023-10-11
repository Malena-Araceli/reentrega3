from django.shortcuts import render
from Curso.models import camadaCurso
from Curso.forms import CamadaCursoForm, EstudianteForm, ProfesorForm, EntregableForm

def inicio (request):
    return render(request, "Curso/index.html")

#def curso (request):
 #   return render(request, "Curso/curso.html")

#def profesores (request):
 #   return render(request, "Curso/profesores.html")

#def estudiantes (request):
    #return render(request, "Curso/estudiantes.html")

#def entregables (request):
    #return render(request, "Curso/entregables.html")

#def entregables (request):
    #return render(request, "Curso/entregables.html")


def curso(request):
    if request.method == "POST":
        form = CamadaCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Curso/index.html")
    else:
        form = CamadaCursoForm()
    return render(request, "Curso/curso.html", {'form': form})


def estudiantes(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Curso/index.html")
    else:
        form = EstudianteForm()
    return render(request, "Curso/estudiantes.html", {'form': form})

def profesores(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Curso/index.html")
    else:
        form = ProfesorForm()
    return render(request, "Curso/profesores.html", {'form': form})

def entregables(request):
    if request.method == "POST":
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Curso/index.html")
    else:
        form = EntregableForm()
    return render(request, "Curso/entregables.html", {'form': form})