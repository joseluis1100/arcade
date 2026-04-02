# Questão 36

Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo: 

| Venda mensal | Comissão | 
|:---|:---| 
| Maior ou igual a R$100.000,00 | R$700,00 + 16% das vendas | 
| Menor que R$100.000,00 e maior ou igual a R$80.000,00 | R$650,00 + 14% das vendas | 
| Menor que R$80.000,00 e maior ou igual a R$60.000,00 | R$600,00 + 14% das vendas | 
| Menor que R$60.000,00 e maior ou igual a R$40.000,00 | R$550,00 + 14% das vendas | 
| Menor que R$40.000,00 e maior ou igual a R$20.000,00 | R$500,00 + 14% das vendas | 
| Menor que R$20.000,00 | R$400,00 +14% das vendas |

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float vendas;
    scanf("%f", &vendas);
    if(vendas >= 100000) {
        printf("%.2f\n", 700 + vendas * 0.16);
    } else if(vendas >= 80000) {
        printf("%.2f\n", 650 + vendas * 0.14);
    } else if(vendas >= 60000) {
        printf("%.2f\n", 600 + vendas * 0.14);
    } else if(vendas >= 40000) {
        printf("%.2f\n", 550 + vendas * 0.14);
    } else if(vendas >= 20000) {
        printf("%.2f\n", 500 + vendas * 0.14);
    } else {
        printf("%.2f\n", 400 + vendas * 0.14);
    }
    return 0;
}
```

</details>

[Código](./C/draft.c)
