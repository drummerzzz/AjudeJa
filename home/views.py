from django.shortcuts import render
from django.views.generic import TemplateView
from donatario.forms import GranteeForm
from donatario.models import Grantee

class HomeTemplateView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = GranteeForm()
        context['pedidos'] = Grantee.objects.all()
        return context
    
    

class DetailTemplateView(TemplateView):
    template_name = "home/detalhe.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pedido_id = self.request.GET.get('pedido', None)
        pedido = Grantee.objects.filter(id=pedido_id)[0]
        context["pedido"] = pedido
        return context
    
