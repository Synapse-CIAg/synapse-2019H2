---
marp: true
paginate: true
backgroundImage: url('../../assets/background.png');
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

# Programação Imperativa

##### Éttore Leandro Tognoli

---

# Agenda

- Variáveis e Atribuição
- Operações e Comparações
- Estruturas de Controle
- Estruturas de Repetição
- Funções
- Entrada e Saída

---

<!-- footer: Programação Imperativa -->
<!-- header: Números Binários -->


# Variáveis e Atribuição

```python
var1 = 1
var2 = 1.5
var3 = 'l'
var4 = 'teste'
var5 = True

```
---

# Variáveis e Atribuição

```c
int var1 = 1;
long var1 = 1;
short var1 = 1;
float var2 = 1.5;
double var2 = 1.5;
char var3 = 'l';
char* var4 = "teste";
bool var5 = true;
```
---
# Variáveis e Atribuição

```python
var1 = 1
var2 = var1
var1 = 2
```
---

# Variáveis e Atribuição

```c
int var1 = 1;
int var2 = var1;
var1 = 2;
```

---

# Variáveis

Declaração
Tipo

---

# Atribuição

Destrutivo

---

# Operações Matemáticas

```python

a = 1
b = 12
c = -13

delta = b ** 2 - 4 * a * c
x0 = (-b + delta**0.5) / 2 * a
x1 = (-b - delta**0.5) / 2 * a

```

---

# Operações Matemáticas

```c
#include <math.h>

double a = 1.;
double b = 12.;
double c = -13.;

int main(int argc, char ** argv) {
    double delta = pow(b,2.) - 4. * a * c;
    double x0 = (-b + pow(delta,0.5)) / 2. * a;
    double x1 = (-b - pow(delta,0.5)) / 2. * a;
}

```

---

# Operações Booleanas

```python

a = True
b = False

a or b
a and b

```

---

# Operações Booleanas


```c

bool a = true;
bool b = false;

a || b;
a && b;

```

---

# Operações Binárias

```python

a = 127
b = 15
a & b
a | b
a ^ b
a << 1
b >> 1

```
---

# Operações Binárias

```c
unsigned char a = 127;
unsigned char b = 15;

int main(int argc, char ** argv) {
    a & b;
    a | b;
    a ^ b;
    a << 1;
    b >> 1;
}
```
---

# Comparações

```python

a = 10
b = 5

a > b
a >= b
a < b
a <= b
a != b
a == b

```

---

# Comparações

```c
int a = 10;
int b = 5;

int main(int argc, char** argv) {
    a > b;
    a >= b;
    a < b;
    a <= b;
    a == b;
    a != b;
}
```
---

# Estruturas de Controle

```python

if True:
    pass

```

---

# Estruturas de Controle

```python

if True:
    pass
else:
    pass

```
---

# Estruturas de Controle

```c
int main(int argc, char** argv){
    if(true){

    }
    else{

    }
}

```

---

# Estruturas de Controle

```c
int value = 1;

int main(int argc, char** argv){
    switch(value){
        case 1:
        // ...
        break;
        default:
        // ...
    }
}

```
---

# Estruturas de Repetição

```python
while True:
    pass
```

---
# Estruturas de Repetição

```python
counter = 0
while counter < 10:
    counter += 1

```
---
# Estruturas de Repetição

```c
int main(int argc, char** argv){
    int counter = 0;
    while(counter < 10){
        counter += 1;
    }
}

```
---
# Estruturas de Repetição

```c
int main(int argc, char** argv){
    int counter = 0;
    do {
        counter += 1;
    }
    while(counter < 10);
}

```
---

# Estruturas de Repetição

```c
int main(int argc, char** argv){
    for(int counter=0;counter<10;counter+=1){
        
    }
}

```
---


<!-- header: Programação Imperativa -->

# Obrigado!

![bg 50%](https://i.pinimg.com/originals/50/5a/d3/505ad3c84cc53ef72fe113191580a23c.gif)
