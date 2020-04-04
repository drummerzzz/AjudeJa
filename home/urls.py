from django.urls import path
from home.views import HomeTemplateView, DetailTemplateView, Base

app_name = 'home'

urlpatterns = [
  path('', HomeTemplateView.as_view()),
  path('detalhes/', DetailTemplateView.as_view(), name="detalhe"),
  path('home/', Base.as_view(), name="home")
]
