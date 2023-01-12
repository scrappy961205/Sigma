import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

Indicadores_Unidad_Medida_Choices = (
    ('dia', 'Dias'),
    ('mes', 'Meses'),
    ('ano', 'Años'),
)
Estado_Choices = (
    ('realizado', 'Realizado'),
    ('aplazado', 'Aplazado'),
    ('pendiente', 'Pendiente'),
)


class Plan(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre del Plan')
    descripcion = models.TextField(max_length=500, verbose_name='Descripción del plan')
    acciones_estrategica_id = models.ManyToManyField('AccionEstrategica', verbose_name='Acción estrategica')
    tareas_id = models.ManyToManyField('Tarea', verbose_name='Tareas')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'TB_PLan'
        default_permissions = []
        permissions = ()
        ordering = ['-id']


class AccionEstrategica(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la Acción Estratégica')
    descripcion = models.TextField(max_length=500, verbose_name='Descripción de la acción estratégica')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'TB_AccionEstrategica'
        default_permissions = []
        permissions = ()
        ordering = ['-id']


class Tarea(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la Tarea')
    descripcion = models.TextField(max_length=500, verbose_name='Descripción de la tarea')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'TB_Tarea'
        default_permissions = []
        permissions = ()
        ordering = ['-id']


class Meta(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la Meta')
    descripcion = models.TextField(max_length=500, blank = True, verbose_name='Descripción de la meta')
    indicador_id = models.ForeignKey('Indicador', on_delete=models.CASCADE, null=True, blank=True,
                                     verbose_name='Indicadores')
    acciones_estrategica_id = models.ForeignKey('AccionEstrategica', on_delete=models.CASCADE, null=True, blank=True,
                                                verbose_name='Acciones')
    organismo_id = models.ForeignKey('Organismo', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Organismo')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'TB_Meta'
        default_permissions = []
        permissions = ()
        ordering = ['-id']


class Indicador(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre del Indicador')
    descripcion = models.TextField(max_length=500, blank = True, verbose_name='Descripción del indicador')
    unidad_medida = models.CharField(max_length=200, verbose_name='U/M')

    def __str__(self):
        return self.unidad_medida

    class Meta:
        db_table = 'TB_Indicador'
        default_permissions = []
        permissions = ()
        ordering = ['-id']


class Accion(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la Acción')
    area_id = models.ForeignKey('AreaPriorizada', on_delete=models.CASCADE, verbose_name='Áreas Priorizadas')
    organismo_id = models.ForeignKey('Organismo', on_delete=models.CASCADE, verbose_name='Organismo')
    tarea_id = models.ForeignKey('Tarea', on_delete=models.CASCADE, verbose_name='Tarea')
    presupuesto = models.DecimalField(max_digits=9, decimal_places=2, default=0,
                                      validators=[MinValueValidator(0, message='El importe debe ser positivo')],
                                      verbose_name='Presupuesto')
    financiamiento = models.DecimalField(max_digits=9, decimal_places=2, default=0,
                                         validators=[MinValueValidator(0, message='El importe debe ser positivo')],
                                         verbose_name='Financiamiento')
    fuente_financimiento = models.CharField(max_length=200, verbose_name='Fuente de financiamiento')
    estado = models.CharField(max_length=15, choices=Estado_Choices, verbose_name='Estado de la acción')
    observacion = models.CharField(max_length=500, verbose_name='Observaciones')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'TB_Accion'
        default_permissions = []
        permissions = ()
        ordering = ['-id']


class Organismo(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre del Organismo')
    descripcion = models.TextField(max_length=500, blank = True, verbose_name='Descripción del organismo')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'TB_Organismo'
        default_permissions = []
        permissions = ()
        ordering = ['-id']


class AreaPriorizada(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre del Área')
    descripcion = models.TextField(max_length=500, verbose_name='Descripción del área')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'TB_Area'
        default_permissions = []
        permissions = ()
        ordering = ['-id']
