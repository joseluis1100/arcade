# Questão 05

Façaa um programa que receba um numero inteiro e verifique se este numero é par ou ímpar.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#include <math.h>

int main() {
    int numero;
    scanf("%d", &numero);

    /* 
    Para saber se um numero é par dividimos ele por 2 e o resto dessa operação tem que ter 0 como resultado.
    E o número ímpar, ao ser divido por 2, o resto é 1. Logo, o que nos interessa é apenas o resto da operação
    */
    if (numero % 2 == 0) {
        printf("%d é par\n", numero);
    } else {
        printf("%d é ímpar\n", numero);
    }

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
4
======== EXPECT
4 é par
<<<<<<<< FINISH

>>>>>>>> INSERT
7
======== EXPECT
7 é ímpar
<<<<<<<< FINISH

>>>>>>>> INSERT
0
======== EXPECT
0 é par
<<<<<<<< FINISH

>>>>>>>> INSERT
-2
======== EXPECT
-2 é par
<<<<<<<< FINISH

>>>>>>>> INSERT
13
======== EXPECT
13 é ímpar
<<<<<<<< FINISH
```


[Código](./C/draft.c)
