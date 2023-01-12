# coding=utf-8
from django import forms
from django_filters import FilterSet, CharFilter, ChoiceFilter, BooleanFilter, DateFilter

from apps.sigma_metas.models import Accion

text_widget = forms.TextInput(attrs={'class': 'form-control'})
boolean_widget = forms.Select(attrs={'class': 'form-control'},
                              choices=[('', 'Desconocido'), (True, 'Si'), (False, 'No')])
date_inicio_widget = forms.TextInput(
    attrs={'class': 'form-control fecha_inicio begin-range', 'placeholder': 'Mayor o igual que...'})
date_fin_widget = forms.TextInput(
    attrs={'class': 'form-control fecha_fin end-range', 'placeholder': 'Menor o igual que...'})
date_widget = forms.TextInput(
    attrs={'class': 'form-control fecha', 'placeholder': 'Igual a...'})
date_fecha_widget = forms.TextInput(
    attrs={'class': 'form-control fecha begin-range', 'placeholder': 'Mayor o igual que...'})
date_fin_fecha_widget = forms.TextInput(
    attrs={'class': 'form-control fecha end-range', 'placeholder': 'Menor o igual que...'})


def get_widget(widget=forms.TextInput, extra=None, choices=None):
    attrs = {'class': 'form-control'}
    if isinstance(widget, forms.Select):
        return forms.Select(attrs={'class': 'form-control'}, choices=choices)
    else:
        if extra is not None:
            for key, value in extra.iteritems():
                attrs[key] = value
        return widget(attrs=attrs)



class ReporteAccionlol(FilterSet):
    # area=DateFilter(
    #
    # )
    class Meta:
        model = Accion
        fields = ['area_id']


class Reportfnanciamientolol(FilterSet):
    class Meta:
        model = Accion
        fields = ['estado']

# class ReporteDiasConfirmadosRentaAgencia(FilterSet):
#     fecha_inicio=DateFilter(
#         name='fk_cmrd__mes',
#         lookup_expr='gte',
#         label='Fecha Inicio',
#         widget=get_widget(widget=forms.DateInput,
#                           extra={
#                               'placeholder':'Mayor o igual que ...',
#                               'autocomplete': 'off',
#                               'class':
#                                   'form-control fecha_inicio_reporte begin-range'
#                           }),
#         method='solo_mes',
#
#     )
#     fecha_fin = DateFilter(
#         name='fk_cmrd__mes',
#         lookup_expr='gte',
#         label='Fecha Fin',
#         widget=get_widget(widget=forms.DateInput,
#                           extra={
#                                  'placeholder': 'Menor o igual que ...',
#                               'autocomplete': 'off',
#                               'class':
#                                   'form-control fecha_inicio_reporte begin-range'
#                           }),
#         method='solo_anno'
#     )
#
#     class Meta:
#         model = CMRDCategoria
#         fields = ['fk_cmr__fk_cliente']
#     def solo_mes(self,queryset,name,value):
#         return queryset.filter(fk_cmrd__mes=value.month, fk_cmrd__ano=value.year)
#
#     def solo_anno(self,queryset,name,value):
#         return queryset.filter(fk_cmrd__ano=value.year)
#
#     def __init__(self, *args, **kwargs):
#         super(ReporteDiasConfirmadosRentaAgencia, self).__init__(*args, **kwargs)
#         self.form.initial['load_from'] = datetime.datetime.today().replace(day=1)
#         self.form.initial['load_to'] = datetime.datetime.today()
#         if self.data == {}:
#             self.queryset = self.queryset.none()