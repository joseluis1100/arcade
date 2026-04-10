# Faça um programa para verificar

Faça um programa para verificar se um determinado numero inteiro e divisível por 3 ou 5, mas não simultaneamente pelos dois.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int numero;
    scanf("%d", &numero);
    
    if (numero % 3 == 0 && numero % 5 == 0) {
        printf("Inválido: número divisível por 3 e 5\n");
        return 0;
    } else if (numero % 3 == 0 || numero % 5 == 0) {
        printf("%d é divisivel por 3 ou 5\n", numero);
        return 0;
    }
    
    printf("Inválido: número não divisível por 3 ou 5\n");
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
15
======== EXPECT
Inválido: número divisível por 3 e 5
<<<<<<<< FINISH

>>>>>>>> INSERT
9
======== EXPECT
9 é divisivel por 3 ou 5
<<<<<<<< FINISH

>>>>>>>> INSERT
10
======== EXPECT
10 é divisivel por 3 ou 5
<<<<<<<< FINISH

>>>>>>>> INSERT
6
======== EXPECT
6 é divisivel por 3 ou 5
<<<<<<<< FINISH

>>>>>>>> INSERT
30
======== EXPECT
Inválido: número divisível por 3 e 5
<<<<<<<< FINISH
```


[Código](./C/draft.c)
