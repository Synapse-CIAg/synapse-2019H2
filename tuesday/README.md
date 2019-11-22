# Cronograma

- [Intro 24/09/2019](#intro-24092019)
- [Basic concepts 01/10/2019](#basic-concepts-01102019)
- [First task 08/10/2019](#first-task-08102019)
- [Second task 12/11/2019](#second-task-12112019)
- [Third task 19/11/2019](#third-task-19112019)
- [Unknown 26/11/2019](#unknown-26112019)
- [Unknown 03/12/2019](#unknown-03122019)

## Intro 24/09/2019

* What is Reactive Programming
* What problems can it solve

## Basic concepts 01/10/2019

* Intro to Rx
* Transforming
* Filtering
* Combining

## First task 08/10/2019

* Build a simple HTML page that:

    * Has an input
    * While the user is typing into the input, display a list of suggestions below it 

## Second task 12/11/2019

Criar uma página HTML simples de login com

* Dois inputs (usuário e senha)
* Um botão

Comportamento:

* O botão deverá ser habilitado somente quando o usuário e senha digitados forem válidos

Validação:

* Usuário: 3 caracteres, conter um `@`
* Senha: 3 caracteres

Sugestão de operador:
https://www.learnrxjs.io/operators/combination/combinelatest.html

## Third task 19/11/2019

Criar um mecanismo de polling, que consultará uma API REST a cada 4 segundos - utilizando RxJS

O polling deverá conter uma estratégia de `retry` de forma exponencial (backoff exponencial). Sempre que a API retornar um código de erro, o algoritmo sempre deve esperar o dobro de tempo para tentar novamente.

## Unknown 26/11/2019

## Unknown 03/12/2019
