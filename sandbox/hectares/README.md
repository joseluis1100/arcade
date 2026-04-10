# Valor de área em metros

Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares. A fórmula de conversão é: H = M ∗ 0,0001, sendo M a área em metros quadrados e H a área em hectares.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float m;
    scanf("%f", &m);
    float h = m * 0.0001;
    printf("%f\n", h);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10000.0
======== EXPECT
1.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0
======== EXPECT
0.000100
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
50000.0
======== EXPECT
5.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
0.010000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
