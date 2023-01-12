from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from apps.mixins import JefePermissionRequiredMixin
from apps.sigma_metas.forms import AreaPriorizadaForm
from apps.sigma_metas.models import AreaPriorizada

class AreaPriorizadaListView(LoginRequiredMixin,ListView):
    model = AreaPriorizada
    template_name = 'area/area_list.html'
    queryset = AreaPriorizada.objects.all()
    success_url = reverse_lazy('sigma:area_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:area_create')
        context['entity'] = 'Area Priorizada'
        context['title'] = 'Listado de las areas priorizadas'
        return context

class AreaPriorizadaCreateView(JefePermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = AreaPriorizada
    template_name = 'form.html'
    form_class = AreaPriorizadaForm
    success_url = reverse_lazy('sigma:area_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:area_create')
        context['entity'] = 'Area Priorizada'
        context['title'] = 'Crear un area priorizada'
        context['list_url'] = self.success_url
        return context


class AreaPriorizadaUpdateView(JefePermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = AreaPriorizada
    template_name = 'form.html'
    form_class = AreaPriorizadaForm
    success_url = reverse_lazy('sigma:area_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:area_create')
        context['entity'] = 'Area Priorizada'
        context['title'] = 'Actualizar un area priorizada'
        context['list_url'] = self.success_url
        return context


class AreaPriorizadaDeleteView(JefePermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = AreaPriorizada
    template_name = 'delete.html'
    success_url = reverse_lazy('sigma:area_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:area_create')
        context['entity'] = 'Area Priorizada'
        context['title'] = 'Eliminar area priorizada'
        context['list_url'] = self.success_url
        return context