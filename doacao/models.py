from django.db import models
from django.conf import settings

class Donation(models.Model):
    name = models.CharField("Nome", max_length=50)
    sexo = models.CharField("Sexo", max_length=1, choices=settings.SEXO_CHOICE)