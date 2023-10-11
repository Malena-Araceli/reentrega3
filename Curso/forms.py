
from django import forms
from .models import camadaCurso, Estudiante, Profesor, Entregable

class CamadaCursoForm(forms.ModelForm):
    class Meta:
        model = camadaCurso
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = '__all__'
