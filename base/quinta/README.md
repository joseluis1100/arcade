# Questão 05

Leia um numero real e imprima a quinta parte desse numero.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float x;
    scanf("%f", &x);

    // Quando uma expressão mistura tipos: int e float, em C, o int é convertido para float para evitar perda de precisão.
    // Nessa questão, X é float e 5 int, logo esse resultado será um float.
    float quinta_parte = x / 5.0;
    printf("%f\n", quinta_parte);

    return 0;
    /* Caso aconteça de serem duas variáveis int e você deseje que o resultado seja um float, 
    basta converter apenas uma das variáveis (cast), que o restante da expressão também será convertida para float.
    EX:
    int x = 11;
    int y = 2;
    float divisao = (float) x / y; // resultado = 5.50000
    */
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
25.0
======== EXPECT
5.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
2.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
7.5
======== EXPECT
1.500000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
20.000000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
