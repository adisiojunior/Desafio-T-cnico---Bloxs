# myapp/serializers.py
from rest_framework import serializers
from .models.pessoa import Pessoa
from .models.conta import Conta
from .models.transacao import Transacao
from .enum import TipoConta

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class ContaSerializer(serializers.ModelSerializer):
    tipo_conta = serializers.ChoiceField(choices=[(tag.value, tag.name) for tag in TipoConta])

    class Meta:
        model = Conta
        fields = '__all__'


class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'


class TransacaoSerializer(serializers.ModelSerializer):
    saldo_anterior = serializers.ReadOnlyField()
    saldo_posterior = serializers.ReadOnlyField()
    tipo_transacao = serializers.CharField(max_length=255)
    data_transacao = serializers.DateTimeField()

    class Meta:
        model = Transacao
        fields = '__all__'