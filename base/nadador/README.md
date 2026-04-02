# Questão 27

Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias: 

| Categoria | Idade | 
|:---|:---| 
| Infantil A | 5 a 7 | 
| Infantil B | 8 a 10 | 
| Juvenil A | 11 a 13 | 
| Juvenil B | 14 a 17 | 
| Sênior | maiores de 18 anos |

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int idade;
    scanf("%d", &idade);
    // ordem de maior para menor para evitar condições desnecessárias
    if(idade >= 18) {
        printf("Senior\n");
    } else if(idade >= 14) {
        printf("Juvenil B\n");
    } else if(idade >= 11) {
        printf("Juvenil A\n");
    } else if(idade >= 8) {
        printf("Infantil B\n");
    } else if(idade >= 5) {
        printf("Infantil A\n");
    } else {
        printf("Muito novo\n");
    }
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
20
======== EXPECT
Senior
<<<<<<<< FINISH

>>>>>>>> INSERT
15
======== EXPECT
Juvenil B
<<<<<<<< FINISH

>>>>>>>> INSERT
12
======== EXPECT
Juvenil A
<<<<<<<< FINISH

>>>>>>>> INSERT
9
======== EXPECT
Infantil B
<<<<<<<< FINISH

>>>>>>>> INSERT
6
======== EXPECT
Infantil A
<<<<<<<< FINISH

>>>>>>>> INSERT
3
======== EXPECT
Muito novo
<<<<<<<< FINISH
```


[Código](./C/draft.c)
