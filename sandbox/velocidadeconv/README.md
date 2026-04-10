# Velocidade em m/s (metros por

Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilometros por hora). A fórmula de conversão é: K = M ∗ 3.6, sendo K a velocidade em km/h e M em m/s.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float M;
    scanf("%f", &M);

    float K = M * 3.6;
    printf("%f\n", K);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10.0
======== EXPECT
36.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
27.78
======== EXPECT
100.008003
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
20.0
======== EXPECT
72.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0
======== EXPECT
3.600000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
