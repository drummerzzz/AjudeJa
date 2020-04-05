from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from donatario.forms import GranteeForm
from donatario.models import Grantee
from doador.models import Donor
from doacao.models import Donation

class HomeTemplateView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = GranteeForm()
        context['pedidos'] = Grantee.objects.filter(atendido=False)
        return context


class ListTemplateView(TemplateView):
    
    template_name = "home/lista.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedidos'] = Grantee.objects.filter(atendido=False)
        return context
    

class DetailView(View):
    
    template_name = "home/detail.html"
    
    def get(self, request, *args, **kwargs):
        context = {}
        pedido_id = request.GET.get('pedido', None)
        pedido = Grantee.objects.filter(id=pedido_id)[0]
        context["pedido"] = pedido
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        pedido_id = request.GET.get('pedido', None)
        pedido = Grantee.objects.filter(id=pedido_id)[0]
        doador, created = Donor.objects.get_or_create(
            nome=request.POST.get('nome'),
            whatsapp=request.POST.get('whatsapp')
        )
        Donation.objects.create(
            doador=doador,
            donatario=pedido
        )
        pedido.atender()
        context["pedido"] = pedido
        context["ajudado"] = True
        return render(request, self.template_name, context)
    

class Obrigado(TemplateView):
    template_name = "ui/obrigado.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["form"] = GranteeF?orm()
        # context['pedidos'] = Gr?antee.objects.all()
        context['pedido'] = Grantee.objects.first()
        return context
