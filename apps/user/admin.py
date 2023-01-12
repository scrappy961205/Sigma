from django.contrib import admin

# Register your models here.
from apps.user.models import Usuario

admin.site.register(Usuario)