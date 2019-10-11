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
_paginate: false
---

<!-- _backgroundImage: url('../../../assets/raw-background.png'); -->
# API

## Aula 01 - Conceitos inicias

##### Leandro Augusto Ragni

<!-- footer: API aula 01 -->

---

# Agenda

### 1. O que é uma API?
### 2. API ou Library
### 3. API significado
### 4. API objetivo
### 5. Tipos de API
### 6. APIs públicas e privadas
### 7. WebAPI

---

# Itens

### 8. WebAPI: JSON - XML
### 9. REST
### 10. Princípios REST
### 11. REST e RESTful
### 12. Ferramentas para testarmos APIs
### 13 Python

---

# O que é API?

De forma simples, é uma aplicação com foco principal fornecer recursos para outra aplicação.

Uma API pode oferecer parte dos dados e serviços de uma empresa sem abrir mão do controle.

Exemplo: Login por redes sociais.

---

# API ou Library

O fato de ser uma aplicação e não um encapsulamento de código dentro da mesma aplicação diferencia API de uma biblioteca.

---

# API significado

API - Application Programming Interface
Em português seria interface de programação de aplicações.

Uma API oferece recursos abstraindo os detalhes da implemntação.

---

# API objetivos

- Integração entre aplicações (um backend para a aplicação web e para o aplicativo mobile)
- Reuso
- Centralização

---

# Tipos de API

- APIs locais: DLL - Dynamic-link library - Classes ou códigos compilados incorporados em um arquivo dll, que de acordo com as regras de visibilidade aplicadas podem ser usadas por aplicações terceiras.

- WebAPI: aplicações web que fornecerão recursos para outras aplicações.

---

# APIs públicas e privadas

- Públicas possuem acesso liberado, mas podem ter limitação de uso, por exemplo: "Restringir o número de requisições em um determinado tempo".

- Privadas possuem acesso restrito, usadas apenas internamente por uma empresa.

---

# WebAPI

- Recursos disponibilizados pela web.

- Acesso via protocolo HTTP

- Mas o que é HTTP?
  - É um protocolo baseado em texto, que define as regras de trocas de mensagens entre servidores e clientes.

- Exemplos de códigos de resposta:
  - 200 - sucesso;
  - 404 - recurso não encontrado;
  - 500 - erro interno de servidor.

---

# WebAPI: JSON - XML

- JSON é mais utilizado, possui uma forma mais simples e com menos caracteres, mais leve tornando a comunicação mais rápida.

Exemplo:

``` json
{
    "clientes": [
        {
            "nome": "João",
            "idade": 30
        },
        {
            "nome": "Maria",
            "idade": 25
        }
    ]
}
```
---

# WebAPI: JSON - XML

``` XML

<clientes>
    <cliente>
        <nome>João</nome>
        <idade>30</idade>
    </cliente>
    <cliente>
        <nome>Maria</nome>
        <idade>25</idade>
    </cliente>
</clientes>

```

---

# REST

- REST: Representational State Transfer
  - É um modelo de arquitetura;
  - Define principios para criação de recursos;

--- 

# Princípios REST

### As URIs devem possuir nomes significativos de acordo com o recurso por exemplo:
    - www.synapse.com/alunos
    - www.synapse.com/professores
    - www.synapse.com/materias
    - www.synapse.com/materias/1

### As URIs não devem indicar a operação realizada no recurso
    - www.synapse.com/alunos/cadastrar
    - www.synapse.com/alunos/joao/excluir

### As URIs não devem exibir o tipo de representação
    - www.synapse.com/alunos/10/json

---

# Princípios REST

### Utilização dos métodos HTTP
    - GET (obter recurso)
    - POST (cadastrar recurso)
    - PUT (alterar informações do recurso)
    - DELETE (excluir recurso)

### Evitar utilizar somente o método POST

---

# REST e RESTful

Uma aplicação que segue todos os principios REST é chamada de RESTful.

---

# Ferramentas para testarmos APIs

- Postman
- Insomnia

---

# Python

## https://falconframework.org/

sudo apt-get install python-pip
pip install falcon --user
pip install gunicorn --user