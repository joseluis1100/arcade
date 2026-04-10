# Numero inteiro

Leia um numero inteiro e imprima o seu antecessor e o seu sucessor.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int numero;
    scanf("%d", &numero);

    int antecessor = numero - 1;
    int sucessor = numero + 1;
    printf("%d %d\n", antecessor, sucessor);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10
======== EXPECT
9 11
<<<<<<<< FINISH

>>>>>>>> INSERT
0
======== EXPECT
-1 1
<<<<<<<< FINISH

>>>>>>>> INSERT
-5
======== EXPECT
-6 -4
<<<<<<<< FINISH

>>>>>>>> INSERT
1
======== EXPECT
0 2
<<<<<<<< FINISH

>>>>>>>> INSERT
100
======== EXPECT
99 101
<<<<<<<< FINISH
```

[Código](./C/draft.c)
