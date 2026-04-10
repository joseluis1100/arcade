# Angulo em radianos

Leia um angulo em radianos e apresente-o convertido em graus. A fôrmula de conversão é: G = R ∗ 180/π, sendo G o ângulo em graus e R em radianos e π = 3.14.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#define PI 3.14159

int main() {
    float R;
    scanf("%f", &R);

    // Usa a constante PI definida acima
    float G = R * 180.0 / PI;
    printf("%f\n", G);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
3.14159
======== EXPECT
180.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
1.5708
======== EXPECT
90.000282
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.7854
======== EXPECT
45.000141
<<<<<<<< FINISH

>>>>>>>> INSERT
6.28318
======== EXPECT
360.000000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
