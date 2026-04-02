# Questão 24

Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A fórmula de conversão é: A = M ∗ 0,000247, sendo M a área em metros quadrados e A a área em acres.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float m;
    scanf("%f", &m);
    float a = m * 0.000247;
    printf("%f\n", a);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10000.0
======== EXPECT
2.470000
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0
======== EXPECT
0.000247
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
4048.58
======== EXPECT
0.999999
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
0.024700
<<<<<<<< FINISH
```

[Código](./C/draft.c)
