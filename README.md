# Sistema de Gerenciamento de Eventos

Este projeto é um sistema de gerenciamento de eventos desenvolvido com Django Rest Framework (DRF). Ele permite a criação, atualização, exclusão e listagem de informações dos eventos, bem como a criação, atualização e remoção de usuários para registro como participantes de eventos e notificações sobre atualizações dos mesmos eventos.

## Funcionalidades

1. CRUD de Usuários
2. CRUD de Eventos
3. Inscrição de Participantes
4. Notificações para Participantes
5. Relatórios

## Requisitos

- Python 3.12
- Django 5.0.6
- Django Rest Framework 3.15.2
- DRF-Spectacular 0.27.2
- Celery 5.4.0
- Redis 5.0.6
- Pillow 10.3.0

## Configuração do Ambiente

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/fxbrartur/freelaw_events_manager.git
cd freelaw_events_manager
```

### Passo 2: Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate
```
### Passo 3: Instalar as Dependências

```bash
pip install -r requirements.txt
```

Verifique se as dependências são compatíveis com seu ambiente local, caso contrário adapte o que for necessário.

### Passo 4: Configurar o Banco de Dados

Edite o arquivo settings.py para configurar seu banco de dados, se necessário. O projeto está configurado para usar o SQLite por padrão como já vem no Django.

### Passo 5: Executar Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### Passo 6: Inicialização e Testes

Certifique-se de que o Redis esteja em execução na porta 6379:
```bash
redis-server
```

Em uma nova aba, execute o Servidor de Desenvolvimento:
```bash
python manage.py runserver
```

Em uma nova aba, inicie o worker do Celery:
```bash
celery -A events_manager worker --loglevel=info
```

Em uma nova aba, execute os testes para certificar-se que está tudo bem instalado e inicializado:
```bash
pytest
```

## Usando a API

##### POST /api/users/ - Para iniciar, primeiramente é necessário criar um usuário:
``` bash
curl -X 'POST' \
  'http://localhost:8000/api/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "example",
  "email": "example@example.com",
  "first_name": "example",
  "last_name": "example",
  "password": "example",
  "image_url": "https://avatars.githubusercontent.com/u/89175768?v=4"
}'
```
Exemplo de output esperado:
``` bash
{
  "id": 3,
  "username": "cvyHOpOsPoBrmA.guNhtZkXjvgdT7wTbxI7yfziUFSi@NaXB",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "created_at": "2024-05-22T23:16:39.561918Z",
  "token": "<seu_token_aqui>"
}
```
O token gerado será utilizado no cabeçalho para autorização dos requests nos demais endpoints.

## Documentação dos Endpoints

### Swagger
A documentação interativa da API pode ser acessada através do Swagger na seguinte URL: http://localhost:8000/api/schema/swagger-ui/


### Endpoints Disponíveis

A API fornece os seguintes endpoints:

#### Eventos: 

<details>
  <summary>GET /api/events/ - Lista todos os eventos disponíveis</summary>

Request de exemplo:
``` bash
curl -X 'GET' \
  'http://localhost:8000/api/events/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>'
```

Exemplo de output esperado:

``` bash
[
  {
    "id": 2,
    "title": "string",
    "description": "string",
    "date": "2024-06-21",
    "time": "20:01:00",
    "location": "ali",
    "created_at": "2024-06-20T21:49:28.119172Z",
    "updated_at": "2024-06-21T16:07:16.073321Z"
  },
  {
    "id": 3,
    "title": "Test",
    "description": "test",
    "date": "2025-06-22",
    "time": "20:21:00",
    "location": "acula",
    "created_at": "2024-06-20T21:49:41.620780Z",
    "updated_at": "2024-06-20T21:52:19.406385Z"
  }
]
```
</details>

<details>
  <summary>POST /api/events/ - Cria um novo evento</summary>

Request de exemplo:
``` bash
curl -X 'POST' \
  'http://localhost:8000/api/events/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "string",
  "description": "string",
  "date": "2024-06-21",
  "time": "20:21",
  "location": "string"
}'
```

Exemplo de output esperado:

``` bash
{
  "id": 5,
  "title": "string",
  "description": "string",
  "date": "2024-06-21",
  "time": "20:21:00",
  "location": "string",
  "created_at": "2024-06-21T16:25:24.533303Z",
  "updated_at": "2024-06-21T16:25:24.533326Z"
}
```

</details>

<details>
  <summary>GET /api/events/{id}/ - Trazer informações de um evento específico</summary>

``` bash
curl -X 'GET' \
  'http://localhost:8000/api/events/1/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>'
```
Exemplo de output esperado:
``` bash
{
  "id": 1,
  "title": "Evento Teste",
  "description": "Descrição do evento",
  "date": "2024-06-22",
  "time": "15:00:00",
  "location": "Local do evento",
  "created_at": "2024-06-20T20:00:00.000000Z",
  "updated_at": "2024-06-21T15:00:00.000000Z"
}
```
</details>

<details>
  <summary>PUT /api/events/{id}/ - Atualiza um evento específico</summary>

```bash
curl -X 'PUT' \
  'http://localhost:8000/api/events/2/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "string",
  "description": "string",
  "date": "2024-04-24",
  "time": "20:01",
  "location": "local1"
}'
```
Exemplo de output esperado:
``` bash
{
  "id": 2,
  "title": "string",
  "description": "string",
  "date": "2024-06-21",
  "time": "20:01:00",
  "location": "local1",
  "created_at": "2021-03-03T21:49:28.119172Z",
  "updated_at": "2024-04-24T16:32:11.832852Z"
}
```

</details>

<details>
  <summary>DELETE /api/events/{id}/ - Exclui um evento específico</summary>

```bash
curl -X 'DELETE' \
  'http://localhost:8000/api/events/3/' \
  -H 'accept: */*' \
  -H 'Authorization: Token <seu_token_aqui>' \
```
Exemplo de output esperado:
``` bash
status = 204 - No response body
```

</details>

<details>
  <summary>GET /api/events/{id}/report/ - Gera relatório de um evento específico</summary>

```bash
curl -X 'GET' \
  'http://localhost:8000/api/events/4/report/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>'
```
Exemplo de output esperado:
``` bash
{
  "event": "event1",
  "participant_count": 2,
  "participants": [
    {
      "first_name": "ela",
      "last_name": "dela",
      "email": "nela@example.com",
      "image": ""
    },
    {
      "first_name": "ele",
      "last_name": "dele",
      "email": "nele@example.com",
      "image": "profile_pics/156056254v4"
    }
  ]
}
```

</details>

<details>
  <summary>POST /api/events/{id}/subscribe/ - Permite a inscrição de usuários em eventos</summary>

```bash
curl -X 'POST' \
  'http://localhost:8000/api/events/2/subscribe/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>>' \
  -d ''
```
Exemplo de output esperado:
``` bash
{
  "status": "subscribed"
}
```

</details>

#### Usuários:

<details>
  <summary>GET /api/users/ - Traz informações do usuário logado</summary>

```bash
curl -X 'GET' \
  'http://localhost:8000/api/users/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>'
```
Exemplo de output esperado:
``` bash
[
  {
    "id": 3,
    "username": "cvyHOpOsPoBrmA.guNhtZkXjvgdT7wTbxI7yfziUFSi@NaXB",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "created_at": "2024-03-11T11:56:39.561918Z",
    "token": "<seu_token_aqui>"
  }
]
```
</details>  
<details>
  <summary>POST /api/users/ - Cria um novo usuário</summary>

``` bash
curl -X 'POST' \
  'http://localhost:8000/api/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "example",
  "email": "example@example.com",
  "first_name": "example",
  "last_name": "example",
  "password": "example",
  "image_url": "https://avatars.githubusercontent.com/u/89175768?v=4"
}'
```
Exemplo de output esperado:
``` bash
{
  "id": 3,
  "username": "cvyHOpOsPoBrmA.guNhtZkXjvgdT7wTbxI7yfziUFSi@NaXB",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "created_at": "2023-02-11T23:16:39.561918Z",
  "token": "<seu_token_aqui>"
}
```
O token gerado será utilizado no cabeçalho para autorização dos requests nos demais endpoints.
</details>  

<details>
  <summary>GET /api/users/{id}/ - Traz informações dum usuário específico</summary>
Endpoint administrativo, para um superadmin gerenciar os usuários da ferramenta no futuro:

```bash
curl -X 'GET' \
  'http://localhost:8000/api/users/3/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>'
```
Exemplo de output esperado:

```bash
{
  "id": 3,
  "username": "cvyHOpOsPoBrmA.guNhtZkXjvgdT7wTbxI7yfziUFSi@NaXB",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "created_at": "2023-02-11T23:16:39.561918Z",
  "token": "<seu_token_aqui>"
}
```

</details>  

<details>
  <summary>PUT /api/users/{id}/ - Atualiza um usuário específico</summary>

```bash
curl -X 'PUT' \
  'http://localhost:8000/api/users/3/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token <seu_token_aqui>' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "123",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "password": "string"
}'
```
Exemplo de output esperado:

```bash
{
  "id": 3,
  "username": "123",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "created_at": "2024-06-21T14:56:39.561918Z",
  "token": <seu_token_aqui>
}
```

</details>  

<details>
  <summary>DELETE /api/users/{id}/ - Exclui um usuário específico</summary>

```bash
curl -X 'DELETE' \
  'http://localhost:8000/api/users/3/' \
  -H 'accept: */*' \
  -H 'Authorization: Token <seu_token_aqui>' \
```
Exemplo de output esperado:
```bash
status = 204 - No response body
```

</details>  

## Observações

- Os microsserviços, implementei tudo que julguei que seria mais pesado na vida real, e também o que não precisava dar retorno imediato. Foram: Geração de Relatórios de Eventos, Confirmação de Inscrição em Evento, e Notificação de Atualização de Eventos. As notificações e confirmações estão sendo representadas por prints no log do worker do Celery, claro que num cenário real trocaríamos isso para um SMTP (ou outra coisa), até deixei pré-configurado no settings.py já.

<br>

- Trazendo apenas exemplos de output de sucesso para que a documentação não fique muito grande, mas sim, implementei algumas situações de ERROR HANDLING.

<br>

- Com tempo, faria uma configuração de permissões para usuários, onde traria um comportamento mais realístico, do tipo, cada usuário tem propriedade no evento que criou, onde só ele pode editar e apagar o seu próprio evento, ou quando apagado e/ou editado por outro gerasse um pedido de aprovação.
