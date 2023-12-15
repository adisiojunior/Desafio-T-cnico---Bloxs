# Desafio Técnico - Bloxs

## Sobre o Desafio

Nosso desafio consiste em desenvolver uma API que realize operações bancárias básicas e uma aplicação web simples que possibilite realizar as operações via API. Abaixo estão as principais diretrizes:

### Escopo Mínimo:

#### Back-end (API):

- Implementar endpoint que realiza a criação de uma conta;
- Implementar endpoint que realiza o login;
- Implementar endpoint que realiza operação de depósito em uma conta;
- Implementar endpoint que realiza operação de consulta de saldo em determinada conta;
- Implementar endpoint que realiza operação de saque em uma conta;
- Implementar endpoint que realiza o bloqueio de uma conta;
- Implementar endpoint que recupera o extrato de transações de uma conta.

#### Front-end:

- Utilize sua criatividade para desenvolver uma aplicação web que conecte com a API e possibilite que o usuário logue e realize as operações financeiras acima.

### Desenvolver os Recursos em API Rest:

#### Entidade Conta:

- `id_conta`: Numérico
- `id_pessoa`: Numérico
- `saldo`: Monetário
- `limite_saque_diario`: Monetário
- `flag_ativo`: Condicional
- `tipo_conta`: Numérico
- `data_criacao`: Data

#### Tabela de Transações realizadas na conta:

- `id_transacao`: Numérico
- `id_conta`: Numérico
- `valor`: Monetário
- `data_transacao`: Data

#### Tabela de Pessoas:

- `id_pessoa`: Numérico
- `nome`: Texto
- `cpf`: Texto
- `data_nascimento`: Data

*Observação:* Não é necessário realizar operações com a tabela pessoa, mas é necessária a criação da tabela para mapeamento da relação com a conta e popular tabela "pessoa" com script de migração, utilizando o Flask-Migrate, com pelo menos uma pessoa.

### Etapas Importantes:

3. Certifique-se de revisar seu código, de modo que fique o mais organizado possível para a avaliação e entendimento dos avaliadores.
4. Utilize a estrutura de pastas que achar mais adequada, bem como padrões, patterns, práticas de segurança, performance etc.
5. O diferencial para este desafio é o aprimoramento do mesmo, bem como implementação de práticas de performance e/ou estrutura.

### O que Iremos Avaliar:

- Seu código;
- Dockerfile ou docker-compose do serviço;
- Script de banco;
- Organização;
- Boas práticas;
- Documentação;
- Diferenciais (Ex: Testes, Manual, Performance, tudo o que você fizer de adicional...).

## Tecnologias a Serem Utilizadas:

- Python
- Flask / APIFlask
- Flask-Migrate
- SQLAlchemy / Flask-SQLAlchemy (com MySQL)
- Docker / Docker-Compose
- React, Next.js
