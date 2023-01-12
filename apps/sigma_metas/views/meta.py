from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from apps.mixins import JefePermissionRequiredMixin
from apps.sigma_metas.forms import MetaForm
from apps.sigma_metas.models import Meta

class MetaListView(LoginRequiredMixin,ListView):
    model = Meta
    template_name = 'meta/meta_list.html'
    queryset = Meta.objects.all()
    success_url = reverse_lazy('sigma:meta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:meta_create')
        context['entity'] = 'Meta'
        context['title'] = 'Listado de las metas'
        return context


class MetaCreateView(JefePermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model = Meta
    template_name = 'form.html'
    form_class = MetaForm
    success_url = reverse_lazy('sigma:meta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:meta_create')
        context['entity'] = 'Meta'
        context['title'] = 'Crear una meta'
        context['list_url'] = self.success_url
        return context


class MetaUpdateView(JefePermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Meta
    template_name = 'form.html'
    form_class = MetaForm
    success_url = reverse_lazy('sigma:meta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:meta_create')
        context['entity'] = 'Meta'
        context['title'] = 'Actualizar una meta'
        context['list_url'] = self.success_url
        return context


class MetaDeleteView(JefePermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Meta
    template_name = 'delete.html'
    success_url = reverse_lazy('sigma:meta_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:meta_create')
        context['entity'] = 'Meta'
        context['title'] = 'Eliminar una meta'
        context['list_url'] = self.success_url
        return context