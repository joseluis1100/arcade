# Questão 12

Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é: K = 1,61 ∗ M , sendo K a distância em quilômetros e M em milhas.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float m;
    scanf("%f", &m);
    float k = 1.61 * m;
    printf("%f\n", k);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.0
======== EXPECT
1.610000
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
16.100000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
161.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0
======== EXPECT
8.050000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
