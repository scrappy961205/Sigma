from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from apps.mixins import JefePermissionRequiredMixin
from apps.sigma_metas.forms import PlanForm
from apps.sigma_metas.models import Plan


class PlanListView(LoginRequiredMixin, ListView):
    model = Plan
    template_name = 'plan/plan_list.html'
    queryset = Plan.objects.all()
    success_url = reverse_lazy('sigma:plan_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:plan_create')
        context['entity'] = 'Plan'
        context['title'] = 'Listado de los planes'
        return context


class PlanCreateView(JefePermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Plan
    template_name = 'form.html'
    form_class = PlanForm
    success_url = reverse_lazy('sigma:plan_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:plan_create')
        context['entity'] = 'Plan'
        context['title'] = 'Crear un plan'
        context['list_url'] = self.success_url
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return super(PlanCreateView, self).post(request, *args, **kwargs)


class PlanUpdateView(JefePermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Plan
    template_name = 'form.html'
    form_class = PlanForm
    success_url = reverse_lazy('sigma:plan_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:plan_create')
        context['entity'] = 'Plan'
        context['title'] = 'Actualizar plan'
        context['list_url'] = self.success_url
        return context


class PlanDeleteView(JefePermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Plan
    template_name = 'delete.html'
    success_url = reverse_lazy('sigma:plan_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('sigma:plan_create')
        context['entity'] = 'Plan'
        context['title'] = 'Eliminar plan'
        context['list_url'] = self.success_url
        return context
