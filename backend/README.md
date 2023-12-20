# Backend Django Rest Framework - README

## Overview

This repository contains the backend implementation for a financial application using Django Rest Framework. The backend is organized into three main classes: `Pessoa`, `Account`, and `Transacao`. Additionally, it includes authentication functionalities through the `Auth` class.

### Technologies Used

- Django Rest Framework
- Python 3.8

## Endpoints

### Pessoa

1. **Criar uma Pessoa**
   - Endpoint: `/api/pessoas/criar/`
   - Method: `POST`
   - Description: Cria uma nova pessoa.
![img.png](img.png)

2. **Listar Todas as Pessoas**
   - Endpoint: `/api/pessoas/listar/`
   - Method: `GET`
   - Description: Retorna uma lista de todas as pessoas cadastradas.
![img_1.png](img_1.png)

3. **Listar uma Única Pessoa**
   - Endpoint: `/api/pessoas/{id}/`
   - Method: `GET`
   - Description: Retorna os detalhes de uma única pessoa com base no ID.
![img_2.png](img_2.png)
   
### Account

4. **Criar uma Conta**
   - Endpoint: `/api/accounts/criar/`
   - Method: `POST`
   - Description: Cria uma nova conta.
![img_3.png](img_3.png)
5. **Listar Todas as Contas**
   - Endpoint: `/api/accounts/listar/`
   - Method: `GET`
   - Description: Retorna uma lista de todas as contas cadastradas.
![img_5.png](img_5.png)

6. **Listar Conta por ID**
   - Endpoint: `/api/accounts/{id}/`
   - Method: `GET`
   - Description: Retorna os detalhes de uma conta com base no ID.
![img_4.png](img_4.png)

### Transacao

7. **Realizar Transacao**
   - Endpoint: `/api/transacoes/realizar/`
   - Method: `POST`
   - Description: Realiza uma transação, com o tipo especificado (SAQUE ou DEPOSITO). Se for SAQUE, o valor é deduzido; se for DEPOSITO, o valor é aumentado. Retorna o extrato da transação.
![img_6.png](img_6.png)
8. **Extrato da Transacao**
   - Endpoint: `/api/transacoes/extrato/{id}/`
   - Method: `GET`
   - Description: Retorna o histórico de transações para uma conta específica.
![img_7.png](img_7.png)
### Auth

9. **Login**
   - Endpoint: `/api/auth/login/`
   - Method: `POST`
   - Description: Realiza o login e retorna o token de acesso.
![img_8.png](img_8.png)
10. **Token**
    - Endpoint: `/api/auth/token/`
    - Method: `POST`
    - Description: Retorna o token de acesso e o token de atualização.
![img_9.png](img_9.png)
11. **Refresh Token**
    - Endpoint: `/api/auth/refresh-token/`
    - Method: `POST`
    - Description: Atualiza o token de acesso usando o token de atualização.

## Getting Started

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the development server using `python manage.py runserver`.

Feel free to explore the various endpoints and functionalities provided by the backend.

**Note:** Ensure that you have a working knowledge of Django Rest Framework and have set up the necessary configurations and database connections before running the server.
