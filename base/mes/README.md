# Questão 16

Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este numero. Isto e, janeiro se 1, fevereiro se 2, e assim por diante.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int mes;
    scanf("%d", &mes);
    
    switch (mes) {
    case 1:
        printf("janeiro\n");
        break;
    case 2:
        printf("fevereiro\n");
        break;
    case 3:
        printf("março\n");
        break;
    case 4:
        printf("abril\n");
        break;
    case 5:
        printf("maio\n");
        break;
    case 6:
        printf("junho\n");
        break;
    case 7:
        printf("julho\n");
        break;
    case 8:
        printf("agosto\n");
        break;
    case 9:
        printf("setembro\n");
        break;
    case 10:
        printf("outubro\n");
        break;
    case 11:
        printf("novembro\n");
        break;
    case 12:
        printf("dezembro\n");
        break;
    default:
        printf("Mes invalido\n");
    }
    
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1
======== EXPECT
janeiro
<<<<<<<< FINISH

>>>>>>>> INSERT
2
======== EXPECT
fevereiro
<<<<<<<< FINISH

>>>>>>>> INSERT
3
======== EXPECT
março
<<<<<<<< FINISH

>>>>>>>> INSERT
7
======== EXPECT
julho
<<<<<<<< FINISH

>>>>>>>> INSERT
0
======== EXPECT
Mes invalido
<<<<<<<< FINISH
```


[Código](./C/draft.c)
