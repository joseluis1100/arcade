# Questão 40

Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int dias;
    scanf("%d", &dias);
    float bruto = 30 * dias;
    //100% - 8% = 92% = 0.92
    float liquido = bruto * 0.92;
    printf("%.2f\n", liquido);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10
======== EXPECT
276.00
<<<<<<<< FINISH

>>>>>>>> INSERT
0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
5
======== EXPECT
138.00
<<<<<<<< FINISH

>>>>>>>> INSERT
1
======== EXPECT
27.60
<<<<<<<< FINISH

>>>>>>>> INSERT
100
======== EXPECT
2760.00
<<<<<<<< FINISH
```

[Código](./C/draft.c)
