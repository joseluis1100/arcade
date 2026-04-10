# Faça a leitura de três

Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#include <math.h>

int main() {
    int valor1, valor2, valor3;
    scanf("%d %d %d", &valor1, &valor2, &valor3);
    int somaQuadrados = pow(valor1, 2) + pow(valor2, 2) + pow(valor3, 2);
    printf("%d\n", somaQuadrados);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1 2 3
======== EXPECT
14
<<<<<<<< FINISH

>>>>>>>> INSERT
0 0 0
======== EXPECT
0
<<<<<<<< FINISH

>>>>>>>> INSERT
3 4 5
======== EXPECT
50
<<<<<<<< FINISH

>>>>>>>> INSERT
-1 2 -3
======== EXPECT
14
<<<<<<<< FINISH

>>>>>>>> INSERT
10 10 10
======== EXPECT
300
<<<<<<<< FINISH
```

[Código](./C/draft.c)
