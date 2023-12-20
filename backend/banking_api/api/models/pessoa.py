# myapp/models/pessoa.py
from django.db import models
from validate_docbr import CPF
from django.core.exceptions import ValidationError

def validate_cpf(value):
    cpf = CPF()

    if not cpf.validate(value):
        raise ValidationError('CPF inválido.')

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, blank=False, null=False)
    cpf = models.CharField(max_length=14, unique=True, validators=[validate_cpf])
    data_nascimento = models.DateField()

    def clean(self):
        if self.data_nascimento and self.data_nascimento.year < 1900:
            raise ValidationError('Data de nascimento inválida.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
