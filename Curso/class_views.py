from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import camadaCurso
from django.urls import reverse_lazy

class CursoListView(ListView):
    model = camadaCurso
    template_name = "Curso/class_list.html"


class CursoDetailView(DetailView):
    model = camadaCurso
    template_name = "Curso/class_detail.html"


class CursoCreateView(CreateView):
    """
    Esta clase envía por defecto un formulario al archivo html. Envía los campos indicados en la lista "fields" y podemos hacer uso de dicho formulario bajo la key "form".
    """

    model = camadaCurso
    template_name = "Curso/class_create.html"
    fields = ["nombre", "camada"]

    success_url = reverse_lazy("Profesores")


class CursoUpdateView(UpdateView):
    model = camadaCurso
    success_url = reverse_lazy("List")
    fields = ["id", "nombre", "camada"]
    template_name = "Curso/class_update.html"


class CursoDeleteView(DeleteView):
    model = camadaCurso
    success_url = reverse_lazy("List")
    template_name = 'Curso/class_confirm_delete.html'