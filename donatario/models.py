from django.db import models
from municipios.models import UF, Municipio
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
    estado = models.ForeignKey(UF, on_delete=models.PROTECT, null=True,)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, null=True,)
    atendido = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
    def getPhone(self):
        return self.whatsapp.replace('(','').replace(')','').replace('-','').replace(' ','')
    
    def atender(self):
        self.atendido = True
        super().save()
    
    def situacao(self):
        if self.atendido:
            return "atendido"
        return "Não atendido"