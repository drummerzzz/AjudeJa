from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Donor(models.Model):
    nome = models.CharField("Nome", max_length=50, null=True)
    whatsapp = models.CharField("Whastapp", max_length=20, null=True)
    
    def __str__(self):
        return self.nome