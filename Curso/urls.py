
from django.urls import path
from Curso import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('curso/', views.curso, name="Cursos"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('entregables/', views.entregables, name= "Entregables"),
    path('cursoform/', views.cursoFormulario, name= "cursoForm"),
  
    
]
