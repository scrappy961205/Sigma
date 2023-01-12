from django.contrib.auth.models import Group
from django.db import transaction
from django.forms import ModelForm

from apps.user.models import Usuario


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # solapin = forms.CharField(max_length=7, min_length=7)

    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['groups', 'last_login', 'is_superuser',
                   'is_staff', 'is_active', 'date_joined',
                   'user_permissions']

    # def save(self, commit=True):
    #     data = {}
    #     form = super()
    #     try:
    #         if form.is_valid():
    #             passw = self.cleaned_data['password']
    #             us = form.save(commit=False)
    #             if us.pk is None:
    #                 us.set_password(passw)
    #             else:
    #                 user = User.objects.get(pk=us.pk)
    #                 if user.password != passw:
    #                     us.set_password(passw)
    #             us.save()
    #             data = us
    #         else:
    #             data['error'] = form.errors
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return data
