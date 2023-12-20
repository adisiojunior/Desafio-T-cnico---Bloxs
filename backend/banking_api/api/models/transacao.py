# myapp/models/transacao.py
from django.db import models
from .conta import Conta

class Transacao(models.Model):
    id_transacao = models.AutoField(primary_key=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_anterior = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    saldo_posterior = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    tipo_transacao = models.CharField(max_length=255, default='SAQUE')
    data_transacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transacao {self.id_transacao} - Conta {self.conta.id_conta} - Valor {self.valor}"
