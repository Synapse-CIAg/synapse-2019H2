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
# Arquitetura de Computadores

##### Éttore Leandro Tognoli

---
# Agenda

* Soma
* Subtração
* Multiplexador e Demultiplexador
* ULA
* Memória
* Contador
* Assembly & MIPS

---

# Digital

https://github.com/hneemann/Digital
https://github.com/hneemann/Digital/releases/download/v0.23/Digital.zip

---

<!-- footer: Arquitetura de Computadores -->
<!-- header: ULA -->
# Somador Completo

![](https://upload.wikimedia.org/wikipedia/commons/0/0e/Somador_Completo.JPG)

---
# Somador Completo 4bits

![](https://www.mspc.eng.br/dir61/im01/eldig12_1.png)

---
# Subtração

`7 - 3 = 4` 

`7 + ( 10 - 3 ) = 7 + 7 = 4` 

`5 - 2 = 3` 

`5 + ( 10 - 2 ) = 5 + 8 = 3` 

---
# Subtração

`7 - 3 = 4` 
`0111 - 0011 = 0100` 
`0111 + ( 1100 + 1) = 0111 + 1101 = 1  0100` 

---

# Multiplexador e Demultiplexador

![](https://upload.wikimedia.org/wikipedia/commons/e/e0/Telephony_multiplexer_system.gif)

---
# Multiplexador

| s0 | i1 | i0 | o |
|----|----|----|---|
| 0  | 0  | 0  | 0 |
| 0  | 0  | 1  | 1 |
| 0  | 1  | 0  | 0 |
| 0  | 1  | 1  | 1 |
| 1  | 0  | 0  | 0 |
| 1  | 0  | 1  | 0 |
| 1  | 1  | 0  | 1 |
| 1  | 1  | 1  | 1 |


---
# Demultiplexador

| s0 | i | o1 | o0 |
|----|---|----|----|
| 0  | 0 | 0  | 0  |
| 0  | 1 | 0  | 1  |
| 1  | 0 | 0  | 0  |
| 1  | 1 | 1  | 0  |

---
# ULA

![](http://antigo.fpgaparatodos.com.br/newsite/images/stories/exemplo/ULA/ULA_diagrama.png)

---

<!-- header: Memória -->

# FlipFlop

![](https://upload.wikimedia.org/wikipedia/commons/e/e1/SR_%28Clocked%29_Flip-flop_Diagram.svg)

---

# FlipFlop D

![bg 30%](https://upload.wikimedia.org/wikipedia/commons/8/8c/D-Type_Flip-flop.svg)

---

# MIPS

![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/MIPS_Architecture_%28Pipelined%29.svg/1920px-MIPS_Architecture_%28Pipelined%29.svg.png)

---

# MIPS

https://pt.wikipedia.org/wiki/Arquitetura_MIPS

https://dannyqiu.me/mips-interpreter/
https://visualmips.github.io/
https://rivoire.cs.sonoma.edu/cs351/wemips/

---

<!-- header: Arquitetura de Computadores -->
# Obrigado!

