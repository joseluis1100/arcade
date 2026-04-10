# Número real

Faça um programa que leia um número real e o imprima.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float x;
    //%f é usado para float(números com casa decimal)
    scanf("%f", &x);
    printf("%f\n", x);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10.0
======== EXPECT
10.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
5.5
======== EXPECT
5.500000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
-3.7
======== EXPECT
-3.700000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.123
======== EXPECT
100.123001
<<<<<<<< FINISH
```

[Código](./C/draft.c)
