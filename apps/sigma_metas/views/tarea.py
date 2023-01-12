from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from apps.sigma_metas.forms import TareaForm
from apps.sigma_metas.models import Tarea
from apps.mixins import *

class TareaListView(LoginRequiredMixin,ListView):
    model = Tarea
    template_name = 'tarea/tarea_list.html'
    queryset = Tarea.objects.all()
    success_url = reverse_lazy('sigma:tarea_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:tarea_create')
        context['entity'] = 'Tarea'
        context['title'] = 'Listado de las tareas'
        return context

class TareaCreateView(JefePermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = Tarea
    template_name = 'form.html'
    form_class = TareaForm
    success_url = reverse_lazy('sigma:tarea_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:tarea_create')
        context['entity'] = 'Tarea'
        context['title'] = 'Crear una tarea'
        context['list_url'] = self.success_url
        return context

class TareaUpdateView(JefePermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Tarea
    template_name = 'form.html'
    form_class = TareaForm
    success_url = reverse_lazy('sigma:tarea_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:tarea_create')
        context['entity'] = 'Tarea'
        context['title'] = 'Actualizar tarea'
        context['list_url'] = self.success_url
        return context

class TareaDeleteView(JefePermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Tarea
    template_name = 'delete.html'
    success_url = reverse_lazy('sigma:tarea_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:tarea_create')
        context['entity'] = 'Tarea'
        context['title'] = 'Eliminar una tarea'
        context['list_url'] = self.success_url
        return context