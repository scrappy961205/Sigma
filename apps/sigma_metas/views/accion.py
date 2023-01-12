from django.urls import reverse_lazy
from django.views.generic import *

from apps.mixins import JefePermissionRequiredMixin
from apps.sigma_metas.forms import AccionForm
from apps.sigma_metas.models import Accion
from django.contrib.auth.mixins import LoginRequiredMixin

class AccionListView(LoginRequiredMixin,ListView):
    model = Accion
    template_name = 'accion/accion_list.html'
    queryset = Accion.objects.all()
    success_url = reverse_lazy('sigma:accion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:accion_create')
        context['entity'] = 'Accion'
        context['title'] = 'Listado de las acciones'
        return context


class AccionCreateView(JefePermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = Accion
    template_name = 'form.html'
    form_class = AccionForm
    success_url = reverse_lazy('sigma:accion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:accion_create')
        context['entity'] = 'Accion'
        context['title'] = 'Crear una accion'
        context['list_url'] = self.success_url
        return context


class AccionUpdateView(JefePermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Accion
    template_name = 'form.html'
    form_class = AccionForm
    success_url = reverse_lazy('sigma:accion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:accion_create')
        context['entity'] = 'Accion'
        context['title'] = 'Actualizar accion'
        context['list_url'] = self.success_url
        return context


class AccionDeleteView(JefePermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Accion
    template_name = 'delete.html'
    success_url = reverse_lazy('sigma:accion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:accion_create')
        context['entity'] = 'Accion'
        context['title'] = 'Eliminar accion'
        context['list_url'] = self.success_url
        return context