from django.shortcuts import render
from django.views.generic import CreateView
from donatario.forms import GranteeForm


class DonatarioCreateView(CreateView):
    form_class = GranteeForm
    template_name = "home/home.html"
    success_url = "/"
