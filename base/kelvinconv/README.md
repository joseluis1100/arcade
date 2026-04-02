# Questão 09

Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A formula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float C;
    scanf("%f", &C);

    float K = C + 273.15;
    printf("%f\n", K);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
0.0
======== EXPECT
273.149994
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
373.149994
<<<<<<<< FINISH

>>>>>>>> INSERT
-273.15
======== EXPECT
0.000006
<<<<<<<< FINISH

>>>>>>>> INSERT
25.0
======== EXPECT
298.149994
<<<<<<<< FINISH

>>>>>>>> INSERT
37.0
======== EXPECT
310.149994
<<<<<<<< FINISH
```

[Código](./C/draft.c)
