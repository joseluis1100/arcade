# Valor de area em acres

Leia um valor de area em acres e apresente-o convertido em metros quadrados m². A fórmula de conversão é: M = A ∗ 4048.58 , sendo M a área em metros quadrados e A a área em acres.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float A;
    scanf("%f", &A);

    float M = A * 4048.58;
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
4048.580078
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
40485.800781
<<<<<<<< FINISH

>>>>>>>> INSERT
0.000247
======== EXPECT
0.999999
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
404858.000000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
