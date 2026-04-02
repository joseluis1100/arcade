# Questão 18

Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A fórmula de conversão é: L = 1000 ∗ M , sendo L o volume em litros e M o volume em metros cúbicos.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float m;
    scanf("%f", &m);
    float l = 1000 * m;
    printf("%f\n", l);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.0
======== EXPECT
1000.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.5
======== EXPECT
500.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
2.5
======== EXPECT
2500.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
10000.000000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
