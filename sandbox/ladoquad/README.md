# Tamanho do lado de um

Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
// #include <math.h> // Se for utilizar a função pow(lado, 2)

int main() {
    float lado;
    scanf("%f", &lado);

    // Multiplicar lado * lado é muito mais simples (e leve para o processador)
    // do que usar a função pow()!
    float area = lado * lado;
    printf("%.2f\n", area);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
5.0
======== EXPECT
25.00
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
3.5
======== EXPECT
12.25
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
100.00
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0
======== EXPECT
1.00
<<<<<<<< FINISH
```

[Código](./C/draft.c)
