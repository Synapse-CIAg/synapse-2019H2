---
marp: true
paginate: true
#footer: Copyright © 2019, Éttore Leandro Tognoli
_paginate: false
---

# Lógica Computacional

##### Éttore Leandro Tognoli

---

<!-- header: Lógica Computacional -->

# Agenda

- Números Binários
- Algebra Booleana
- Soma de Produtos & Produto de Somas
- Axiomas
- Mapa de Karnaugh

---

<!-- header: Números Binários -->

# Números Binários

---

# Representação Decimal

| Milhar | Centena | Dezena | Unidade |      |
| ------ | ------- | ------ | ------- | ---- |
| 1      | 2       | 3      | 4       | 1234 |

---

# Representação Decimal

| Milhar = 10 ^ 3 | Centena= 10 ^ 2 | Dezena= 10 ^ 1 | Unidade = 10 ^ 0 |      |
| --------------- | --------------- | -------------- | ---------------- | ---- |
| 1               | 2               | 3              | 4                | 1234 |

```
1 * 10 ^ 3 + 2 * 10 ^ 2 + 3 * 10 ^ 1 + 4 * 10 ^ 0 = 1234
```

---

# Binário para Decimal

| 2 ^ 3 | 2 ^ 2 | 2 ^ 1 | 2 ^ 0 |               |     |
| ----- | ----- | ----- | ----- | ------------- | --- |
| 0     | 0     | 0     | 0     | 0 + 0 + 0 + 0 | 0   |
| 0     | 0     | 0     | 1     | 0 + 0 + 0 + 1 | 1   |
| 0     | 0     | 1     | 0     | 0 + 0 + 2 + 0 | 2   |
| 0     | 1     | 0     | 0     | 0 + 4 + 0 + 0 | 4   |
| 1     | 0     | 0     | 0     | 8 + 0 + 0 + 0 | 8   |

---

# Binário para Decimal

| 2 ^ 3 | 2 ^ 2 | 2 ^ 1 | 2 ^ 0 |      |      |
| ----- | ----- | ----- | ----- | ---- | ---- |
| 1     | 0     | 1     | 0     | \_\_ | \_\_ |
| 1     | 0     | 0     | 1     | \_\_ | \_\_ |
| 1     | 1     | 1     | 0     | \_\_ | \_\_ |
| 1     | 1     | 1     | 1     | \_\_ | \_\_ |
| 1     | 0     | 0     | 1     | \_\_ | \_\_ |

---

# Decimal para Binário

Conversão do 14, divisão sucessivas por 2

|       |       |       |       |       |     |
| ----- | ----- | ----- | ----- | ----- | --- |
|       | 14    | _2_   |
| Resta | **0** | 7     | _2_   |
|       | Resta | **1** | 3     | _2_   |
|       |       | Resta | **1** | 1     | _2_ |
|       |       |       | Resta | **1** | 0   |
|       |       |       |       |       | FIM |

Utlizar os restos de forma inversa, **1110**

---

<!-- header: Algebra Booleana -->

# Algebra Booleana

---

# Lócica _Não_

| A   | Y   |
| --- | --- |
| 0   | 1   |
| 1   | 0   |

![bg 80%](https://www.tutorialspoint.com/digital_circuits/images/not_gate.jpg)

---

# Lócica _E_

| A   | B   | Y   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 0   |
| 1   | 0   | 0   |
| 1   | 1   | 1   |

![bg 80%](https://www.tutorialspoint.com/digital_circuits/images/and_gate.jpg)

---

# Lócica _OU_

| A   | B   | Y   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 1   |

![bg 80%](https://www.tutorialspoint.com/digital_circuits/images/or_gate.jpg)

---

# Lócica _OU Exclusivo_

| A   | B   | Y   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 0   |

![bg 80%](https://www.tutorialspoint.com/digital_circuits/images/exor_gate.jpg)

---

# Lócica _OU Exclusivo Negado_

| A   | B   | Y   |
| --- | --- | --- |
| 0   | 0   | 1   |
| 0   | 1   | 0   |
| 1   | 0   | 0   |
| 1   | 1   | 1   |

![bg 80%](https://www.tutorialspoint.com/digital_circuits/images/exnor_gate.jpg)

---

<!-- header: Soma de Produtos -->

# Soma de Produtos

---

# XOR

| A   | B   | Y     | Produto |
| --- | --- | ----- | ------- |
| 0   | 0   | 0     |         |
| 0   | 1   | **1** | `A'.B`  |
| 1   | 0   | **1** | `A.B'`  |
| 1   | 1   | 0     |         |

`A'.B + A.B'`

---

<!-- header: Produto de Somas -->

# Produto de Somas

---

# XOR

| A   | B   | Y     | Somas     |
| --- | --- | ----- | --------- |
| 0   | 0   | **0** | `A + B`   |
| 0   | 1   | 1     |           |
| 1   | 0   | 1     |           |
| 1   | 1   | **0** | `A' + B'` |

`( A + B ).( A' + B' )`

---

<!-- header: Axiomas -->

# Axiomas

---

# Elemento Neutro

`A + 0 = A`
`A . 1 = A`

---

# Elemento Absorvente

`A + 1 = 1`
`A . 0 = 0`

---

# Idempotência

`A + A = A`
`A . A = A`

---

# Involução

`(A')' = A`

---

# Complementaridade

`A + A' = 1`
`A . A' = 0`

---

# Comutatividade

`A + B = B + A`
`A . B = B . A`

---

# Associatividade

`(A + B) + C = A + (B + C)`
`(A . B) . C = A . (B . C)`

---

# Distributividade

`A . ( B + C ) = A.B + A.C`
`A + ( B . C ) = (A + B) . ( A + C)`

---
