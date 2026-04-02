# Questão 52

Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float amigo1, amigo2, amigo3, premio;
    scanf("%f %f %f %f", &amigo1, &amigo2, &amigo3, &premio);
    float pesoTotal = amigo1 + amigo2 + amigo3;
    float ganha1 = premio * amigo1 / pesoTotal;
    float ganha2 = premio * amigo2 / pesoTotal;
    float ganha3 = premio * amigo3 / pesoTotal;
    printf("%.2f %.2f %.2f\n", ganha1, ganha2, ganha3);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10.0 20.0 30.0 1200.0
======== EXPECT
200.00 400.00 600.00
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0 100.0 100.0 3000.0
======== EXPECT
1000.00 1000.00 1000.00
<<<<<<<< FINISH

>>>>>>>> INSERT
50.0 25.0 25.0 1000.0
======== EXPECT
500.00 250.00 250.00
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0 2.0 3.0 600.0
======== EXPECT
100.00 200.00 300.00
<<<<<<<< FINISH
```

[Código](./C/draft.c)
