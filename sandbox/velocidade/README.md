# Velocidade em km por hora

Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float k;
    scanf("%f", &k);
    float m = k/3.6;
    printf("%f\n", m);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
36.0
======== EXPECT
10.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
27.777779
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
72.0
======== EXPECT
20.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0
======== EXPECT
0.277778
<<<<<<<< FINISH
```

[Código](./C/draft.c)
