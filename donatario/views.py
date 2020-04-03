from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView
from donatario.forms import GranteeForm

class DonatarioCreateView(CreateView):
    form_class = GranteeForm
    template_name = "home/home.html"
    success_url = "/#ajuda"
    
    def get_success_url(self):
        messages.success(self.request, "Seu pedido foi enviado com sucesso e já está disponível na fila de pedidos.")
        return self.success_url
