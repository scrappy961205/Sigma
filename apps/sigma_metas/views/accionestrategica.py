from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from apps.mixins import JefePermissionRequiredMixin
from apps.sigma_metas.forms import AccionEstrategicaForm
from apps.sigma_metas.models import AccionEstrategica

class AccionEstrategicaListView(LoginRequiredMixin,ListView):
    model = AccionEstrategica
    template_name = 'accion_estrategica/accion_estrategica_list.html'
    queryset = AccionEstrategica.objects.all()
    success_url = reverse_lazy('sigma:accion_estrategica_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:accion_estrategica_create')
        context['entity'] = 'Accion Estrategica'
        context['title'] = 'Listado de las acciones estrategicas'
        return context

class AccionEstrategicaCreateView(JefePermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = AccionEstrategica
    template_name = 'form.html'
    form_class = AccionEstrategicaForm
    success_url = reverse_lazy('sigma:accion_estrategica_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:accion_estrategica_create')
        context['entity'] = 'Accion Estrategica'
        context['title'] = 'Crear una accion estrategica'
        context['list_url'] = self.success_url
        return context


class AccionEstrategicaUpdateView(JefePermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = AccionEstrategica
    template_name = 'form.html'
    form_class = AccionEstrategicaForm
    success_url = reverse_lazy('sigma:accion_estrategica_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:accion_estrategica_create')
        context['entity'] = 'Accion Estrategica'
        context['title'] = 'Actualizar una accion estrategica'
        context['list_url'] = self.success_url
        return context


class AccionEstrategicaDeleteView(JefePermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = AccionEstrategica
    template_name = 'delete.html'
    success_url = reverse_lazy('sigma:accion_estrategica_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:accion_estrategica_create')
        context['entity'] = 'Accion Estrategica'
        context['title'] = 'Eliminar una accion estrategica'
        context['list_url'] = self.success_url
        return context