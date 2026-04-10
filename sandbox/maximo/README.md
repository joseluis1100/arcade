# Escreva um programa que, dados

Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
// biblioteca stdlib obtem o abs() que permite calcular o valor absoluto
#include <stdlib.h>

int main() {
    int n1, n2, maior;
    scanf("%d %d", &n1, &n2);
    
    if (n1 > n2) {
        maior = n1;
        printf("%d\n", maior);
    } else {
        maior = n2;
        printf("%d\n", maior);
    }
    
    int diferenca = abs(n1 - n2);
    printf("%d\n", diferenca);

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1 2 3
======== EXPECT
2
1
<<<<<<<< FINISH

>>>>>>>> INSERT
3 2 1
======== EXPECT
3
1
<<<<<<<< FINISH

>>>>>>>> INSERT
2 3 1
======== EXPECT
3
1
<<<<<<<< FINISH

>>>>>>>> INSERT
5 5 5
======== EXPECT
5
0
<<<<<<<< FINISH

>>>>>>>> INSERT
-1 -2 -3
======== EXPECT
-1
1
<<<<<<<< FINISH
```


[Código](./C/draft.c)
