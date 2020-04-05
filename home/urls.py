from django.urls import path
from home.views import HomeTemplateView, DetailView, ListTemplateView, Obrigado

app_name = 'home'

urlpatterns = [
  path('', HomeTemplateView.as_view()),
  path('detalhes/', DetailView.as_view(), name="detalhe"),
  path('lista/', ListTemplateView.as_view(), name="list"),
  path('obrigado/', Obrigado.as_view(), name="home")
]
 