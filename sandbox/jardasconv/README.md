# Valor de comprimento em metros

Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula de conversão é: J = M / 0.91 , sendo J o comprimento em jardas e M o comprimento em metros.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float M;
    scanf("%f", &M);

    float J = M / 0.91;
    printf("%f\n", J);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
0.91
======== EXPECT
1.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
10.989011
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
109.890106
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0
======== EXPECT
5.494505
<<<<<<<< FINISH
```

[Código](./C/draft.c)
