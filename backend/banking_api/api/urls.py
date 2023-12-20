# myapp/urls.py
from django.urls import path

from .views.pessoa_views import CriarPessoaView, ListarPessoasView
from .views.conta_views import ListarContasView, CriarContaView
from .views.transacao_views import TransacaoView, ExtratoTransacaoView, DetalhesTransacaoView
from .views.auth_views import LoginView, CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('criar_pessoa/', CriarPessoaView.as_view(), name='criar_pessoa'),
    path('listar_pessoas/', ListarPessoasView.as_view(), name='listar_pessoas'),
    path('pessoas/<int:pessoa_id>/', ListarPessoasView.as_view(), name='detalhes_pessoa'),


    path('criar_conta/', CriarContaView.as_view(), name='criar_conta'),
    path('listar_contas/', ListarContasView.as_view(), name='listar_contas'),
    path('conta/<int:conta_id>/', ListarContasView.as_view(), name='detalhes_conta'),

    path('transacao/', TransacaoView.as_view(), name='transacao'),
    path('extrato_transacao/<int:id_conta>/', ExtratoTransacaoView.as_view(), name='extrato_transacao'),
    path('detalhes_transacao/<int:id_transacao>/', DetalhesTransacaoView.as_view(), name='detalhes_transacao'),

    path('login/', LoginView.as_view(), name='login'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]

