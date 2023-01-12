from django import forms
from django.forms import ModelForm
from datetime import datetime

from apps.sigma_metas.models import *


class OrganismoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Organismo
        fields = '__all__'
        # exclude = ['date_creation', 'user', ]

class AreaPriorizadaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = AreaPriorizada
        fields = '__all__'
        # exclude = ['date_creation', 'user', ]

class PlanForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Plan
        fields = '__all__'
        # exclude = ['date_creation', 'user', ]

class TareaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Tarea
        fields = '__all__'
        # exclude = ['date_creation', 'user', ]

class AccionEstrategicaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = AccionEstrategica
        fields = '__all__'
        # exclude = ['date_creation', 'user', ]

class AccionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Accion
        fields = '__all__'
        # exclude = ['date_creation', 'user', ]

class MetaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Meta
        fields = '__all__'
        # exclude = ['date_creation', 'user', ]

class IndicadorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Indicador
        fields = '__all__'
        # exclude = ['date_creation', 'user', ]

