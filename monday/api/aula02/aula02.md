---
marp: true
paginate: true
backgroundImage: url('../../../assets/background.png'); 
color: #3A3A3A; 
style: |
  header {

      color: #FFFFFF;
      font-weight: bold;

  }
  footer {

      font-weight: bold;
      color: #5A5A5A;

  }
  img {

      background-color: #0000;

  }

  teste {
      color: #fff;
  }
_paginate: false
---

<!-- _backgroundImage: url('../../../assets/raw-background.png'); -->
<!-- footer: -->
# API

##### Leandro Augusto Ragni

---

# Agenda

* Revisão aula 01
* Verbos HTTP
* Status de retorno
* Implementações

<!-- footer: API aula 02 -->

---

# Revisão aula 01

## API

- O que é?
- REST ou RESTful
- API x Library
- Objetivo
- Tipos de API
- WebAPI

---

# Padrões REST

- Utilizar URIs que cotenham nomes referente ao domínio;
- Não utilizar as ações nas URIs:
  - http://www.synapse.com/alunos/cadastrar;
  - http://www.synapse.com/excluir/alunos;
- Utilizar os verbos HTTP.

---

# Verbos HTTP

- GET: Recupera informação
- POST: Insere uma nova informação
- PUT: Atualizar ou alterar um recurso
- DELETE: Excluir recurso

---

# HTTP GET

Usado para recuperar um recurso.

### Exemplo:

www.synapse.com/alunos
Recupera todos os alunos.

www.synapse.com/alunos/1
Recupera o aluno com "id" igual 1.

---

# HTTP GET - Tipos de respostas

| Código | Descrição | Utilização |
| 200 | OK | Quando a requisição obter sucesso |
| 400 | Bad Request | Requisições com informações inválidas |
| 401 | Unauthorized | Requisições que exigem autenticação mas as informações de acesso não foram fornecidas |
| 403 | Forbidden | Para os casos em que o requisitante não tenha permissão de acesso |
| 404 | Not Found | Para requisições inválidas |
| 405 | Method Not Allowed | Quando o verbo indicado na requisição não seja suportado |

---

# HTTP POST

- Normalmente usado para criar um recurso.

### Exemplo:

http://www.synapse.com.br/alunos
Cria um novo aluno.

---

# HTTP POST - Tipos de respostas

| Código | Descrição | Utilização |
| 201 | Created | Quando um recurso é criado com sucesso |

---

# HTTP PUT

- Usado para alterar as informações do recurso.

### Exemplo:

http://www.synapse.com.br/alunos/22
Altera as informações de um aluno com "id" igual a 22.

---

# HTTP PUT - Tipos de respostas

| Código | Descrição | Utilização |
| 200 | OK | Quando a requisição obter sucesso |
| 204 | No content | Quando uma requisição obter sucesso mas não retornar nada no corpo da mensagem |

---

# HTTP DELETE

- Usado para remover um recurso.

### Exemplo:

http://www.synapse.com.br/alunos/22
Exclui um aluno com "id" igual a 22.

---

# HTTP DELETE - Tipos de respostas

| Código | Descrição | Utilização |
| 200 | OK | Quando a requisição obter sucesso |
| 204 | No content | Quando uma requisição obter sucesso mas não retornar nada no corpo da mensagem |

---

# Status de retorno de requisições

| Código | Descrição | Utilização |
| 200 | OK | Quando a requisição obter sucesso |
| 201 | Created | Quando um recurso é criado com sucesso |
| 202 | Accepted | Quando uma requisição é aceita mas ainda está processando e não devolveu o resultado |
| 204 | No content | Quando uma requisição obter sucesso mas não retornar nada no corpo da mensagem |
| 206 | Partial Content | Sucesso mas apenas parte do conteúdo do recurso for devolvido | 

---

# Status de retorno de requisições

| Código | Descrição | Utilização |
| 400 | Bad Request | Requisições com informações inválidas |
| 401 | Unauthorized | Requisições que exigem autenticação mas as informações de acesso não foram fornecidas |
| 403 | Forbidden | Para os casos em que o requisitante não tenha permissão de acesso |
| 404 | Not Found | Para requisições inválidas |
| 405 | Method Not Allowed | Quando o verbo indicado na requisição não seja suportado |

---

# Status de retorno de requisições

| Código | Descrição | Utilização |
| 406 | Not Acceptable | Formato não aceito |
| 415 | Unsupported Media Type | |
| 429 | Too Many Requests | Caso o serviço contenha um limite de requisições e este seja atigindo |
| 500 | Internal Server Error | Quando ocorrem erros no servidor |
| 503 | Service Unavailable | Serviço indisponível |

---

# Implementação

---

# Obrigado!
