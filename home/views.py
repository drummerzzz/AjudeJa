from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from donatario.forms import GranteeForm
from donatario.models import Grantee

class HomeTemplateView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = GranteeForm()
        context['pedidos'] = Grantee.objects.filter(atendido=False)
        return context


class DetailTemplateView(View):
    
    template_name = "home/detalhe.html"
    
    def get(self, request, *args, **kwargs):
        context = {}
        pedido_id = request.GET.get('pedido', None)
        pedido = Grantee.objects.filter(id=pedido_id)[0]
        context["pedido"] = pedido
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pedido_id = request.GET.get('pedido', None)
        pedido = Grantee.objects.filter(id=pedido_id)[0]
        pedido.atender()
        success = f'https://api.whatsapp.com/send?phone=55{{pedido.getPhone}}&text=Ol%C3%A1%2C%20vi%20seu%20pedido%20de%20ajuda%20no%20AjudeJ%C3%A1.org%20e%20gostaria%20de%20ajudar.%20'
        return redirect(success)
    
