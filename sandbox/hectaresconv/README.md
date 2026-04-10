# Valor de área em hectares

Leia um valor de área em hectares e apresente-o convertido em metros quadrados m². A fórmula de conversão é: M = H ∗ 10000, sendo M a area em metros quadrados e H a área em hectares.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float H;
    scanf("%f", &H);

    float M = H * 10000.0;
    printf("%f\n", M);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.0
======== EXPECT
10000.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
100000.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.5
======== EXPECT
5000.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
1000000.000000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
