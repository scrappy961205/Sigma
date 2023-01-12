from django.contrib.auth.mixins import *
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets

from apps.mixins import *
from apps.serializers import UserSerializer
from apps.user.forms import UserForm
from apps.user.models import Usuario


class UserListView(AdminPermissionRequiredMixin, LoginRequiredMixin, generic.ListView ):
    model = Usuario
    template_name = 'user_list.html'
    queryset = Usuario.objects.all()
    success_url = reverse_lazy('user:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('user:user_add')
        context['entity'] = 'Usuario'
        context['title'] = 'Listado de Usuarios'
        return context


class UserCreateView(AdminPermissionRequiredMixin,LoginRequiredMixin, generic.CreateView):
    model = Usuario
    template_name = 'form.html'
    form_class = UserForm
    success_url = reverse_lazy('user:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('user:user_add')
        context['entity'] = 'Usuario'
        context['title'] = 'Crear Usuario'
        context['list_url'] = self.success_url
        return context


class UserUpdateView(AdminPermissionRequiredMixin,LoginRequiredMixin, generic.UpdateView):
    model = Usuario
    template_name = 'form.html'
    form_class = UserForm
    success_url = reverse_lazy('user:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('user:user_add')
        context['entity'] = 'Usuario'
        context['title'] = 'Editar Usuario'
        context['list_url'] = self.success_url
        return context


class UserDeleteView(AdminPermissionRequiredMixin,LoginRequiredMixin, generic.DeleteView):
    model = Usuario
    template_name = 'delete.html'
    success_url = reverse_lazy('user:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('user:user_add')
        context['entity'] = 'Usuario'
        context['title'] = 'Eliminar Usuario'
        context['list_url'] = self.success_url
        return context


# Serializers
class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
