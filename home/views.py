from django.shortcuts import render
from django.views.generic import TemplateView
from donatario.forms import GranteeForm

class HomeTemplateView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = GranteeForm()
        return context
    