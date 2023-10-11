from django.urls import path
from Curso import views
from Curso import class_views

urlpatterns = [
    
    path('', views.inicio, name="inicio"),
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('cursos/', views.curso, name="curso"),
    path('entregables/', views.entregables, name="entregables"),
    path('class-list/', class_views.CursoListView.as_view(), name="List"),
   
]