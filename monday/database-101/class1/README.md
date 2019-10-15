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

<!-- _backgroundImage: url('../../assets/raw-background.png'); -->
# Banco de Dados

##### Diego Pereira da Silva

---
<!-- footer: Bando de dados -->

# Agenda

* O que é Banco de Dados
* Tipos de bancos
* Tipos de Bancos de dados
* O que é um Banco de dados SQL
* Como é feito o relacionamento entre tabelas
* Getting Started

---

# Banco de Dados

Coleções organizadas de dados que se relacionam de forma a criar algum sentido (informação) e dar mais eficiência durante uma pesquisa ou estudo.
Antes disso usavam sistemas de arquivos do SO para armazenar informações

---

<!-- footer: Bando de dados -->
# Tipos de Bancos de dados

Durante nossos encontros vamos abordar conceitos e ações do Banco de Dados Relacional (Sql), mas importante saber que existem outros e um pouco de cada conceio

**Alguns tipos:**
* Não relacional (NoSql) 
* Banco de Dados de séries temporais (Time series database)

[Types of database](https://www.tutorialspoint.com/Types-of-databases)

---
# O que é um Banco de dados SQL

Um banco de dados relacional é uma coleção de dados com relacionamentos predefinidos entre si. Esses itens são organizados como um conjunto de tabelas com colunas e linhas. As tabelas são usadas para reter informações sobre os objetos a serem representados no banco de dados

---
# Exemplo de uma tabela
**Tabela pessoa**
| id | nome | cidade_id | idade |
|----|----|----|---|
| 1  | Rafão  | 4  | 22 |
| 2  | Diego  | 3  | 24 |
| 3  | leyverson  | 2  | 72 |
| 4  | Roberto  | 1  | 55 |

mas qual a cidade?

---
# Relacionamento
**Table cidade**
| id | nome | 
|----|----|----|---|
| 1  | Vera Cruz  |
| 2  | Pompeia  |
| 3  | Americana  |
| 4  | Salvador |

---

# Como é feito o relacionamento entre tabelas

* Chave Primária(Pk): No nosso exemplo a chave primária da tabela `cidade` é o `id`
* Chave Estrangeira(Fk): `cidade_id` é nossa fk na tabela `pessoa`

---
# Tipos de Relacionamento

* Um para um
* Um para muitos
* Muitos para muitos

---
# Um para um

São relacionamentos em que uma ocorrencia de uma entidade em A está associada no máximo a uma ocorrencia em uma entidade B e uma ocorrencia na entidade B está associada no máximo a uma ocorrencia na entidade A.
Exemplo: Um `gerente` para cada `departamento`
![](https://sites.google.com/site/uniplibancodedados1/_/rsrc/1348510710650/aulas/aula-7---tipos-de-relacionamento/aula_7_relacionamento3.bmp)


---
# Um para muitos

Ocorre quando uma ocorrência de uma entidade pode se relacionar com várias ocorrências de outra entidade
![](https://sites.google.com/site/uniplibancodedados1/_/rsrc/1348510612033/aulas/aula-7---tipos-de-relacionamento/aula_7_relacionamento.bmp)

---


# Muitos para muitos

Uma ocorrencia de uma entidade em A está associada a qualquer número de ocorrencias na entidade B, e cada ocorrencia da entidade em B está associada a qualquer número de ocorrencias na entidade A.
![](https://sites.google.com/site/uniplibancodedados1/_/rsrc/1348510658318/aulas/aula-7---tipos-de-relacionamento/aula_7_relacionamento2.bmp)

---

# Talk is Cheap

![bg 40%](https://media.giphy.com/media/13bIO859q7xDeo/giphy.gif)

---

# Getting Started

Iremos utilizar docker *caso* não tenha instalado ja em sua máquina

```bash
docker run --name synapse_db -e MYSQL_ROOT_PASSWORD=root -d -p 3306:3306 mysql:5.7.13
mysql -hlocalhost --protocol=TCP -uroot -proot
```

---

# Go on

```sql
SHOW databases;
CREATE DATABASE <name_database>;
USE <name_database>;
SHOW tables;
```

---

# Let's create a TABLE

Vamos criar uma tabela chamada pessoa e setar o `id` como *pk*
```sql
CREATE TABLE person (
    id int PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    document varchar(255) UNIQUE,
    age int
);
```
---



# Insert first value into it

```sql
INSERT INTO person VALUES (1, 'Diego', 'Silva', '40173281800', 24);
```

---

# Select

```sql
SELECT * FROM person;
```

---

# UPDATING A DOC

```sql
UPDATE person SET first_name= "lala" WHERE id = 1;
```
---

# Drop vs Delete vs Truncate
```sql
DROP TABLE table_name; #DELETE TABLE ITSELF
TRUNCATE TABLE table_name; #DELETE DATA ONLY
DELETE FROM table_name WHERE condition; #DELETE DATA WITH CONDITION
```
---


# Obrigado!

