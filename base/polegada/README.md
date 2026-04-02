# Questão 16

Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros. A fórmula de conversão é: C = P ∗ 2,54, sendo C o comprimento em centímetros e P o comprimento em polegadas.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float p;
    scanf("%f", &p);
    float c = p * 2.54;
    printf("%f\n", c);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.0
======== EXPECT
2.540000
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
25.400000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0
======== EXPECT
12.700000
<<<<<<<< FINISH

>>>>>>>> INSERT
12.0
======== EXPECT
30.480000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
