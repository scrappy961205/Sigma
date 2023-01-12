from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

class Startpage(generic.TemplateView):
    # template_name = 'startpage.html'
    template_name = 'login/login.html'


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class Index(generic.TemplateView):
    template_name = 'startpage.html'
    # template_name = 'inicio/index.html'


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)