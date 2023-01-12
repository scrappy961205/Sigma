from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django_filters.views import FilterView

from apps.mixins import JefePermissionRequiredMixin
from apps.sigma_metas.custom_filters import *
from apps.sigma_metas.models import AreaPriorizada


class ReporteAccion(JefePermissionRequiredMixin,LoginRequiredMixin,FilterView):
    model = Accion
    template_name = 'reporte.html'
    filterset_class = ReporteAccionlol

    def get_context_data(self, **kwargs):
        context = super(ReporteAccion, self).get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('index')
        context['entity'] = 'Reporte areas estrategicas'
        context['title'] = 'Reporte de acciones'
        context['all_areas'] = AreaPriorizada.objects.all()
        object_list = self.model.objects.all().filter()
        filter = ReporteAccionlol(self.request.GET, queryset=object_list)
        object_list = filter.qs
        if object_list is not None:
            if self.request.GET:
                get = self.request.GET
                area = get['area_id']
                estado_realizado=[]
                estado_aplazado=[]
                estado_pendiente=[]
                print(object_list)

                if area:
                    for a in object_list:
                        if a.estado=='realizado':
                            estado_realizado.append(a.nombre)
                        elif a.estado == 'aplazado':
                            estado_aplazado.append(a.nombre)
                        else :
                            estado_pendiente.append(a.nombre)
                area_name=AreaPriorizada.objects.get(id=area)
                context.update({
                    'estado_realizado':estado_realizado,
                    'estado_aplazado':estado_aplazado,
                    'estado_pendiente':estado_pendiente,
                    'area':area_name
                })

        return context


class Reportefinanciamiento(JefePermissionRequiredMixin,LoginRequiredMixin, FilterView):
    model = Accion
    template_name = 'reporte_acciones.html'
    filterset_class = Reportfnanciamientolol

    def get_context_data(self, **kwargs):
        context = super(Reportefinanciamiento, self).get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('index')
        context['entity'] = 'Reporte financiamiento'
        context['title'] = 'Reporte de financiamiento'
        object_list = self.model.objects.all().filter()
        filter = ReporteAccionlol(self.request.GET, queryset=object_list)
        object_list = filter.qs

        if object_list is not None:
            if self.request.GET:
                get = self.request.GET
                estado = get['estado_id']
                total_presupuesto = 0
                total_financiamiento = 0
                cumplimiento = 0
                if estado:
                    estado=estado.lower()
                    for a in object_list:
                        if a.estado == estado:
                            total_presupuesto += a.presupuesto
                            total_financiamiento += a.financiamiento
                    if total_presupuesto<=total_financiamiento:
                        cumplimiento=100
                    elif total_presupuesto != 0:
                        cumplimiento = (total_financiamiento + 100) / total_presupuesto
                    else :
                        cumplimiento=0
                context.update({
                    'estado':estado,
                    'total_presupuesto': total_presupuesto,
                    'total_financiamiento': total_financiamiento,
                    'cumplimiento': cumplimiento,
                })
        return context
