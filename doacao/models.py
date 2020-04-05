from django.db import models
from django.conf import settings

class Donation(models.Model):
    avisado = models.BooleanField(default=False)
    doador = models.ForeignKey(
            "doador.Donor", verbose_name="Doador",
            on_delete=models.SET_NULL, blank=True, null=True
        )
    donatario = models.ForeignKey(
        "donatario.Grantee", verbose_name="Donatario",
        on_delete=models.SET_NULL, blank=True, null=True
    )