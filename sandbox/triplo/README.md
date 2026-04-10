# Número inteiro

Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int x;
    scanf("%d", &x);
    int sucessorTriplo = x * 3 + 1;
    int antecessorDobro = x * 2 - 1;
    //também poderia ser: int soma = (x * 3 + 1) + (x * 2 - 1);
    int soma = sucessorTriplo + antecessorDobro;
    printf("%d\n", soma);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1
======== EXPECT
5
<<<<<<<< FINISH

>>>>>>>> INSERT
0
======== EXPECT
0
<<<<<<<< FINISH

>>>>>>>> INSERT
10
======== EXPECT
50
<<<<<<<< FINISH

>>>>>>>> INSERT
-3
======== EXPECT
-15
<<<<<<<< FINISH

>>>>>>>> INSERT
5
======== EXPECT
25
<<<<<<<< FINISH
```

[Código](./C/draft.c)
