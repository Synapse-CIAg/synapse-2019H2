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
- API x Library
- Objetivo
- Tipos de API
- WebAPI

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

### Sucesso HTTP 
- status 200 OK
### Falha:
- status 400 BAD REQUEST
- status 404 NOT FOUND

---

# Obrigado!
