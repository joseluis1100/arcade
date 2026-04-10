# Valor de comprimento em jardas

Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de conversão é: M = 0,91 ∗ J, sendo J o comprimento em jardas e M o comprimento em metros.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float j;
    scanf("%f", &j);
    float m = 0.91 * j;
    printf("%f\n", m);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.0
======== EXPECT
0.910000
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
9.100000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
91.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0
======== EXPECT
4.550000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
