# myapp/views/conta_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.pessoa import Pessoa
from ..models.conta import Conta
from ..serializers import ContaSerializer
from ..enum import TipoConta

import logging

logger = logging.getLogger(__name__)


class ListarContasView(APIView):
    def get(self, request):
        contas = Conta.objects.all()
        serializer = ContaSerializer(contas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CriarContaView(APIView):
    def post(self, request):
        data = request.data
        id_pessoa = data.get('pessoa')

        logger.debug(f'id_pessoa recebido: {id_pessoa}')

        # Verificar se a pessoa existe antes de criar a conta
        if not Pessoa.objects.filter(id_pessoa=id_pessoa).exists():
            logger.debug('Pessoa não encontrada')
            return Response({'error': 'Pessoa não encontrada.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ContaSerializer(data=data)

        try:
            if serializer.is_valid():
                serializer.save()
                logger.debug('Conta criada com sucesso.')
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.error('Erro de validação na serialização da conta.')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            logger.error(f'Erro durante a criação da conta: {str(e)}')
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ListarContasView(APIView):
    def get(self, request, conta_id=None):
        if conta_id:
            try:
                conta = Conta.objects.get(pk=conta_id)
                serializer = ContaSerializer(conta)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Conta.DoesNotExist:
                return Response({'error': 'Conta não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            contas = Conta.objects.all()
            serializer = ContaSerializer(contas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)