from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

CATEGORIA = (
    ("Cesta Básica", "Cesta Básica"),
    ("Remédios", "Remédios"),
    ("EPI's", "EPI's")
)

class Grantee(models.Model):
    nome = models.CharField("Qual seu nome?", max_length=50)
    whatsapp = models.CharField("Qual o número do seu Whatsapp?", max_length=20)
    titulo = models.CharField("Qual o seu pedido de ajuda?", max_length=50)
    categoria = models.CharField("Escolha uma categoria", max_length=50, choices=CATEGORIA, default="Cesta Básica")
    descricao = models.TextField("Descreva o que você está precisando", null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)