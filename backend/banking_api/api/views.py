# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ValidationError
from .models.pessoa import Pessoa
from .serializers import PessoaSerializer

class HelloAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Hello, Django REST Framework!'})


class CriarPessoaView(APIView):
    def post(self, request):
        serializer = PessoaSerializer(data=request.data)

        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ListarPessoasView(APIView):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)