from django.urls import path
from donatario.views import DonatarioCreateView

app_name = 'donatario'

urlpatterns = [
    path('pediodo-de-ajuda/', DonatarioCreateView.as_view(), name='ajuda')
]
