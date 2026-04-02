# Questão 08

Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão é: C = K − 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float k;
    scanf("%f", &k);
    float c = k - 273.15;
    printf("%f\n", c);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
273.15
======== EXPECT
-0.000006
<<<<<<<< FINISH

>>>>>>>> INSERT
373.15
======== EXPECT
99.999992
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
-273.149994
<<<<<<<< FINISH

>>>>>>>> INSERT
300.0
======== EXPECT
26.850000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
-173.149994
<<<<<<<< FINISH
```

[Código](./C/draft.c)
