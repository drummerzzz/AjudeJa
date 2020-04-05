from django.urls import path
from home.views import HomeTemplateView, DetailTemplateView, ListTemplateView, Base

app_name = 'home'

urlpatterns = [
  path('', HomeTemplateView.as_view()),
  path('detalhes/', DetailTemplateView.as_view(), name="detalhe"),
  path('lista/', ListTemplateView.as_view(), name="list"),
  path('home/', Base.as_view(), name="home")
]
 