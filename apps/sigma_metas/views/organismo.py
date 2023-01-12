from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from apps.mixins import JefePermissionRequiredMixin
from apps.sigma_metas.forms import OrganismoForm
from apps.sigma_metas.models import Organismo

class OrganismoListView(LoginRequiredMixin,ListView):
    model = Organismo
    template_name = 'organismo/organismo_list.html'
    queryset = Organismo.objects.all()
    success_url = reverse_lazy('sigma:organismo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:organismo_create')
        context['entity'] = 'Organismo'
        context['title'] = 'Listado de los organismos'
        return context


class OrganismoCreateView(JefePermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = Organismo
    template_name = 'form.html'
    form_class = OrganismoForm
    success_url = reverse_lazy('sigma:organismo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:organismo_create')
        context['entity'] = 'Organismo'
        context['title'] = 'Crear un organismo'
        context['list_url'] = self.success_url
        return context


class OrganismoUpdateView(JefePermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Organismo
    template_name = 'form.html'
    form_class = OrganismoForm
    success_url = reverse_lazy('sigma:organismo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:organismo_create')
        context['entity'] = 'Organismo'
        context['title'] = 'Actualizar organismo'
        context['list_url'] = self.success_url
        return context


class OrganismoDeleteView(JefePermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Organismo
    template_name = 'delete.html'
    success_url = reverse_lazy('sigma:organismo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:organismo_create')
        context['entity'] = 'Organismo'
        context['title'] = 'Eliminar Organismo'
        context['list_url'] = self.success_url
        return context