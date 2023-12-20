from django.db import models

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

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

class Transacao(models.Model):
    id_transacao = models.AutoField(primary_key=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_transacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transacao {self.id_transacao} - Conta {self.conta.id_conta} - Valor {self.valor}"
