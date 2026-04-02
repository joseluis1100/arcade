# Questão 23

Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int ano;
    scanf("%d", &ano);
    if(ano % 400 == 0 || (ano % 4 == 0 && ano % 100 != 0)) {
        printf("Eh bissexto\n");
    } else {
        printf("Nao eh bissexto\n");
    }
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
2000
======== EXPECT
Eh bissexto
<<<<<<<< FINISH

>>>>>>>> INSERT
1900
======== EXPECT
Nao eh bissexto
<<<<<<<< FINISH

>>>>>>>> INSERT
2024
======== EXPECT
Eh bissexto
<<<<<<<< FINISH

>>>>>>>> INSERT
2023
======== EXPECT
Nao eh bissexto
<<<<<<<< FINISH

>>>>>>>> INSERT
1996
======== EXPECT
Eh bissexto
<<<<<<<< FINISH
```


[Código](./C/draft.c)
