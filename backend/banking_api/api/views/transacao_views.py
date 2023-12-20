# views/transacao_views.py
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.conta import Conta
from ..models.transacao import Transacao
from ..serializers import TransacaoSerializer

import logging
from decimal import Decimal
from django.utils import timezone

logger = logging.getLogger(__name__)

class TransacaoView(APIView):
    def post(self, request):
        data = request.data
        id_conta = data.get('conta')
        valor = Decimal(data.get('valor'))
        tipo_transacao = data.get('tipo_transacao')  # Pode ser 'DEPOSITO' ou 'SAQUE'

        # Verificar se a conta existe antes de realizar a transação
        try:
            conta = Conta.objects.get(id_conta=id_conta)
        except Conta.DoesNotExist:
            return Response({'error': 'Conta não encontrada.'}, status=status.HTTP_400_BAD_REQUEST)

        # Adicionar as informações adicionais ao dicionário de dados
        data['saldo_anterior'] = conta.saldo
        data['saldo_posterior'] = conta.saldo + valor
        data['data_transacao'] = timezone.now()

        serializer = TransacaoSerializer(data=data)

        try:
            if serializer.is_valid():
                # Atualizar o saldo da conta com base no tipo de transação
                if tipo_transacao == 'DEPOSITO':
                    conta.saldo += valor
                elif tipo_transacao == 'SAQUE':
                    if conta.saldo < valor or valor > conta.limite_saque_diario:
                        return Response({'error': 'Saldo insuficiente ou limite de saque diário ultrapassado.'}, status=status.HTTP_400_BAD_REQUEST)
                    conta.saldo -= valor
                else:
                    return Response({'error': 'Tipo de transação inválido.'}, status=status.HTTP_400_BAD_REQUEST)

                # Salvar a transação e atualizar o saldo da conta
                transacao = serializer.save()

                # Manter a conta salva
                conta.save()

                logger.debug(f'Transação realizada com sucesso: {transacao}')

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f'Erro durante a transação: {str(e)}')
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ExtratoTransacaoView(APIView):
    def get(self, request, id_conta):
        transacoes = Transacao.objects.filter(id_conta=id_conta).order_by('-data_transacao')
        serializer = TransacaoSerializer(transacoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DetalhesTransacaoView(APIView):
    def get(self, request, id_transacao):
        transacao = get_object_or_404(Transacao, id_transacao=id_transacao)

        # Lógica para calcular saldo_anterior e saldo_posterior
        saldo_anterior = transacao.conta.saldo - transacao.valor
        saldo_posterior = saldo_anterior + transacao.valor

        # Atualize os campos no modelo Transacao
        transacao.saldo_anterior = saldo_anterior
        transacao.saldo_posterior = saldo_posterior
        transacao.save()

        serializer = TransacaoSerializer(transacao)
        return Response(serializer.data, status=status.HTTP_200_OK)