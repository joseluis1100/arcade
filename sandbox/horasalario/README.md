# Valor da hora de trabalho

Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float valor_por_hora;
    int horas_trabalhadas;
    scanf("%f %d", &valor_por_hora, &horas_trabalhadas);

    // Multiplicar por 1.10 é o mesmo que adicionar os 10% sobre o valor
    float valor = (valor_por_hora * horas_trabalhadas) * 1.10;

    printf("%.2f\n", valor);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10.0 8
======== EXPECT
88.00
<<<<<<<< FINISH

>>>>>>>> INSERT
20.0 10
======== EXPECT
220.00
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0 0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
15.50 5
======== EXPECT
85.25
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0 1
======== EXPECT
110.00
<<<<<<<< FINISH
```

[Código](./C/draft.c)
