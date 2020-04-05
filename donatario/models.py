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
    email = models.EmailField("Qual seu email?", max_length=254, null=True)
    estado = models.CharField(max_length=200, null=True)
    cidade = models.CharField(max_length=200, null=True)
    titulo = models.CharField("Qual o seu pedido de ajuda?", max_length=50)
    categoria = models.CharField("Escolha uma categoria", max_length=50, choices=CATEGORIA, default="Cesta Básica")
    descricao = models.TextField("Descreva o que você está precisando", null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
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