from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from apps.mixins import JefePermissionRequiredMixin
from apps.sigma_metas.forms import IndicadorForm
from apps.sigma_metas.models import Indicador

class IndicadorListView(LoginRequiredMixin,ListView):
    model = Indicador
    template_name = 'indicador/indicador_list.html'
    queryset = Indicador.objects.all()
    success_url = reverse_lazy('sigma:indicador_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:indicador_create')
        context['entity'] = 'Indicador'
        context['title'] = 'Listado de los indicadores'
        return context


class IndicadorCreateView(JefePermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = Indicador
    template_name = 'form.html'
    form_class = IndicadorForm
    success_url = reverse_lazy('sigma:indicador_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:indicador_create')
        context['entity'] = 'Indicador'
        context['title'] = 'Crear un indicador'
        context['list_url'] = self.success_url
        return context


class IndicadorUpdateView(JefePermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Indicador
    template_name = 'form.html'
    form_class = IndicadorForm
    success_url = reverse_lazy('sigma:indicador_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:indicador_create')
        context['entity'] = 'Indicador'
        context['title'] = 'Actualizar indicador'
        context['list_url'] = self.success_url
        return context


class IndicadorDeleteView(JefePermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Indicador
    template_name = 'delete.html'
    success_url = reverse_lazy('sigma:indicador_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:indicador_create')
        context['entity'] = 'Indicador'
        context['title'] = 'Eliminar indicador'
        context['list_url'] = self.success_url
        return context