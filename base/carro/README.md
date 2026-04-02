# Questão 40

O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor. 

| CUSTO DE FÁBRICA | % DO DISTRIBUIDOR | % DOS IMPOSTOS | 
|:---|:---|:---| 
| até R$12.000,00 | 5 | isento | 
| entre R$12.000,00 e 25.000,00 | 10 | 15 | 
| acima de R$25.000,00 | 15 | 20 |

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float custo, distribuidor, impostos;
    scanf("%f", &custo);
    if(custo > 25000) {
        distribuidor = custo * 0.15;
        impostos = custo * 0.2;
    } else if(custo > 12000) {
        distribuidor = custo * 0.1;
        impostos = custo * 0.15;
    } else {
        distribuidor = custo * 0.05;
        impostos = 0;
    }
    printf("%.2f\n", custo + distribuidor + impostos);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
30000.0
======== EXPECT
40500.00
<<<<<<<< FINISH

>>>>>>>> INSERT
15000.0
======== EXPECT
18750.00
<<<<<<<< FINISH

>>>>>>>> INSERT
10000.0
======== EXPECT
10500.00
<<<<<<<< FINISH

>>>>>>>> INSERT
25000.0
======== EXPECT
31250.00
<<<<<<<< FINISH

>>>>>>>> INSERT
50000.0
======== EXPECT
67500.00
<<<<<<<< FINISH
```


[Código](./C/draft.c)
