from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Donor(models.Model):
    nome = models.CharField("Qual seu nome?", max_length=50, null=True)
    whatsapp = models.CharField("Qual o número do seu Whatsapp?", max_length=20, null=True)