# Questão 07

Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois numeros forem iguais, imprima a mensagem Numeros iguais.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int n1, n2, maior;
    scanf("%d %d", &n1, &n2);
    
    if (n1 > n2) {
        maior = n1;
        printf("%d\n", maior);
        
    // o else if() ocorre quando você quer especificar uma outra condição diferente do primeiro if()
    } else if (n2 > n1) {
        maior = n2;
        printf("%d\n", maior);
        
    // Nesse caso, o else ficou para quando n1 = n2
    } else {
        printf("Numeros iguais\n");
    }

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10 20 30
======== EXPECT
20
<<<<<<<< FINISH

>>>>>>>> INSERT
30 20 10
======== EXPECT
30
<<<<<<<< FINISH

>>>>>>>> INSERT
20 30 10
======== EXPECT
30
<<<<<<<< FINISH

>>>>>>>> INSERT
5 5 5
======== EXPECT
Numeros iguais
<<<<<<<< FINISH

>>>>>>>> INSERT
-1 0 1
======== EXPECT
0
<<<<<<<< FINISH
```


[Código](./C/draft.c)
