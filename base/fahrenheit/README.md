# Questão 07

Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A formula de conversão é: C = 5.0 ∗ (F − 32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float F;
    scanf("%f", &F);

    // Parênteses necessários! Sem eles, a multiplicação e divisão seriam feitas primeiro (hierarquia matemática).
    float C = 5.0 * (F - 32.0) / 9.0;
    printf("%f\n", C);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
32.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
212.0
======== EXPECT
100.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
-40.0
======== EXPECT
-40.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
98.6
======== EXPECT
37.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
77.0
======== EXPECT
25.000000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
