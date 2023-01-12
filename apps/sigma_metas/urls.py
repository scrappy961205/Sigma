from django.contrib import admin
from django.urls import path
from apps.sigma_metas.views.accion import *
from apps.sigma_metas.views.accionestrategica import *
from apps.sigma_metas.views.areapriorizada import *
from apps.sigma_metas.views.indicador import *
from apps.sigma_metas.views.meta import *
from apps.sigma_metas.views.organismo import *
from apps.sigma_metas.views.plan import *
from apps.sigma_metas.views.tarea import *
from apps.sigma_metas.views.reporte import *

app_name='sigma'

urlpatterns = [
    #accion
    path('accion/list/',AccionListView.as_view(), name='accion_list'),
    path('accion/create/',AccionCreateView.as_view(), name='accion_create'),
    path('accion/update/<int:pk>/',AccionUpdateView.as_view(), name='accion_update'),
    path('accion/delete/<int:pk>/',AccionDeleteView.as_view(), name='accion_delete'),

    # accion estrategica
    path('accion/estrategica/list/', AccionEstrategicaListView.as_view(), name='accion_estrategica_list'),
    path('accion/estrategica/create/', AccionEstrategicaCreateView.as_view(), name='accion_estrategica_create'),
    path('accion/estrategica/update/<int:pk>/', AccionEstrategicaUpdateView.as_view(), name='accion_estrategica_update'),
    path('accion/estrategica/delete/<int:pk>/', AccionEstrategicaDeleteView.as_view(), name='accion_estrategica_delete'),

    # area priorizada
    path('area/list/', AreaPriorizadaListView.as_view(), name='area_list'),
    path('area/create/', AreaPriorizadaCreateView.as_view(), name='area_create'),
    path('area/update/<int:pk>/', AreaPriorizadaUpdateView.as_view(), name='area_update'),
    path('area/delete/<int:pk>/', AreaPriorizadaDeleteView.as_view(), name='area_delete'),

    # indicador
    path('indicador/list/', IndicadorListView.as_view(), name='indicador_list'),
    path('indicador/create/', IndicadorCreateView.as_view(), name='indicador_create'),
    path('indicador/update/<int:pk>/', IndicadorUpdateView.as_view(), name='indicador_update'),
    path('indicador/delete/<int:pk>/', IndicadorDeleteView.as_view(), name='indicador_delete'),

    # meta
    path('meta/list/', MetaListView.as_view(), name='meta_list'),
    path('meta/create/', MetaCreateView.as_view(), name='meta_create'),
    path('meta/update/<int:pk>/', MetaUpdateView.as_view(), name='meta_update'),
    path('meta/delete/<int:pk>/', MetaDeleteView.as_view(), name='meta_delete'),

    # organismo
    path('organismo/list/', OrganismoListView.as_view(), name='organismo_list'),
    path('organismo/create/', OrganismoCreateView.as_view(), name='organismo_create'),
    path('organismo/update/<int:pk>/', OrganismoUpdateView.as_view(), name='organismo_update'),
    path('organismo/delete/<int:pk>/', OrganismoDeleteView.as_view(), name='organismo_delete'),

    # plan
    path('plan/list/', PlanListView.as_view(), name='plan_list'),
    path('plan/create/', PlanCreateView.as_view(), name='plan_create'),
    path('plan/update/<int:pk>/', PlanUpdateView.as_view(), name='plan_update'),
    path('plan/delete/<int:pk>/', PlanDeleteView.as_view(), name='plan_delete'),

    # tarea
    path('tarea/list/', TareaListView.as_view(), name='tarea_list'),
    path('tarea/create/', TareaCreateView.as_view(), name='tarea_create'),
    path('tarea/update/<int:pk>/', TareaUpdateView.as_view(), name='tarea_update'),
    path('tarea/delete/<int:pk>/', TareaDeleteView.as_view(), name='tarea_delete'),

    #reportes
    path('reporte/acciones/', ReporteAccion.as_view(), name='reporte_accion'),
    path('reporte/financiamiento/', Reportefinanciamiento.as_view(), name='reporte_financiamiento'),

]
