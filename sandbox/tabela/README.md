# Altura e o peso de

Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostra qual a classificação dessa pessoa. 

| Altura | | Peso | | 
|:---|:---|:---|:---| 
| | Até 60 | Entre 60 e 90 (Inclusive) | Acima de 90 | 
| Menor que 1,20 | A | D | G | 
| De 1,20 a 1,70 | B | E | H | 
| Maior que 1,70 | C | F | I |

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float altura, peso;
    scanf("%f %f", &altura, &peso);
    if(altura > 1.7) {
        if(peso > 90) {
            printf("I\n");
        } else if(peso > 60) {
            printf("F\n");
        } else {
            printf("C\n");
        }
    } else if(altura >= 1.2) {
        if(peso > 90) {
            printf("H\n");
        } else if(peso > 60) {
            printf("E\n");
        } else {
            printf("B\n");
        }
    } else {
        if(peso > 90) {
            printf("G\n");
        } else if(peso > 60) {
            printf("D\n");
        } else {
            printf("A\n");
        }
    }
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.8 95.0
======== EXPECT
I
<<<<<<<< FINISH

>>>>>>>> INSERT
1.5 50.0
======== EXPECT
B
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0 100.0
======== EXPECT
G
<<<<<<<< FINISH

>>>>>>>> INSERT
1.8 70.0
======== EXPECT
F
<<<<<<<< FINISH

>>>>>>>> INSERT
1.5 80.0
======== EXPECT
E
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0 30.0
======== EXPECT
A
<<<<<<<< FINISH
```


[Código](./C/draft.c)
