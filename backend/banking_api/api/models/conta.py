# myapp/models/conta.py
from django.db import models
from .pessoa import Pessoa
from ..enum import TipoConta

class Conta(models.Model):
    id_conta = models.AutoField(primary_key=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    limite_saque_diario = models.DecimalField(max_digits=10, decimal_places=2)
    flag_ativo = models.BooleanField(default=True)
    tipo_conta = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Conta {self.id_conta} - Pessoa {self.pessoa.nome}"
