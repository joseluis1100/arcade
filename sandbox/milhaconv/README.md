# Distancia em quilômetros

Leia uma distancia em quilômetros e apresente-a convertida em milhas. A fórmula de conversão é: M = K / 1.61 , sendo K a distancia em quilômetros M em milhas.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float K;
    scanf("%f", &K);

    float M = K / 1.61;
    printf("%f\n", M);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.61
======== EXPECT
1.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
6.211180
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
62.111801
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0
======== EXPECT
3.105590
<<<<<<<< FINISH
```

[Código](./C/draft.c)
