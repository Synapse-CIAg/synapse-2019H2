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
