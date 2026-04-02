# Questão 35

Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int dia, mes, ano;
    // ao adicionar os / é previsto que a entrada seja no fomato DD/MM/AAAA
    scanf("%d/%d/%d", &dia, &mes, &ano);
    if(dia <= 0 || mes <= 0 || mes > 12) {
        printf("Data invalida.\n");
        return 1;
    }
    // unicos meses com 30 dias são abril, junho, setembro e novembro
    if(mes == 4 || mes == 6 || mes == 9 || mes == 11) {
        if(dia > 30) {
            printf("Data invalida.\n");
            return 1;
        }
    } else if(mes == 2) {
        // um ano é bissexto se for divisível por 400 ou divisível por 4 e não divisível por 100
        if((ano % 400 == 0) || (ano % 4 == 0 && ano % 100 != 0)) {
            if(dia > 29) {
            printf("Data invalida.\n");
            return 1;
            }
        } else {
            if(dia > 28) {
            printf("Data invalida.\n");
            return 1;
            }
        }
    } else {
        if(dia > 31) {
            printf("Data invalida.\n");
            return 1;
            }
    }
    printf("Data valida.\n");
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
15/06/2024
======== EXPECT
Data valida.
<<<<<<<< FINISH

>>>>>>>> INSERT
31/04/2024
======== EXPECT
Data invalida.
<<<<<<<< FINISH

>>>>>>>> INSERT
29/02/2024
======== EXPECT
Data valida.
<<<<<<<< FINISH

>>>>>>>> INSERT
29/02/2023
======== EXPECT
Data invalida.
<<<<<<<< FINISH

>>>>>>>> INSERT
00/05/2024
======== EXPECT
Data invalida.
<<<<<<<< FINISH
```


[Código](./C/draft.c)
