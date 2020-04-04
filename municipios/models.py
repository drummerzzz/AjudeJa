# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models


class UF(models.Model):
    """
    Unidades Federativas (Estados) do Brasil
    """
    id_ibge = models.IntegerField(primary_key=True)
    uf = models.CharField(max_length=2)
    nome = models.CharField(max_length=20)
    regiao = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome


class Municipio(models.Model):
    """
    Municípios do Brasil
    """
    id_ibge = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    nome_abreviado = models.CharField(max_length=150, blank=True, null=True)
    uf = models.ForeignKey(UF, models.PROTECT)
    uf_sigla = models.CharField(max_length=2)
   
    def __str__(self):
        return self.nome
