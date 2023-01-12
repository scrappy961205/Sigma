from django.contrib.auth.models import AbstractUser, Group, User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models, transaction


class Usuario(AbstractUser):
    role = models.CharField(max_length=50, choices=(
        ('client', 'Cliente'),
        ('admin', 'Administrador'),
        ('jefe_proyecto', 'Jefe de Proyecto'),
    ), verbose_name='Rol', null=True, blank=True, default='client')
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.get_full_name() if self.first_name else self.username

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        passw = self.password
        if self.pk is None:
            self.set_password(passw)
        else:
            user = Usuario.objects.get(pk=self.pk)
            if user.password != passw:
                self.set_password(passw)
        super().save()
