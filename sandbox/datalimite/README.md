# Data de nascimento de uma

Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma data válida. Teste se o dia fornecido é um dia válido: dia >0, dia≤28 para o mês de fevereiro (29 se o ano for bissexto), dia≤30 em abril, junho, setembro e novembro, dia 31 nos outros meses. Teste a validade do mês: mês > 0 e mês < 13. Teste a validade do ano: ano <= ano atual (use uma constante definida com o valor igual a 2026). Imprimir: "data válida" ou "data inválida" no final da execução do programa.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#define ANO 2026

int main() {
    int dia, mes, ano;
    scanf("%d/%d/%d", &dia, &mes, &ano);
    // única diferença da questão 35 é a limitação do ano
    if(dia <= 0 || mes <= 0 || mes > 12 || ano > ANO) {
        printf("Data invalida.\n");
        return 1;
    }
    if(mes == 4 || mes == 6 || mes == 9 || mes == 11) {
        if(dia > 30) {
            printf("Data invalida.\n");
            return 1;
        }
    } else if(mes == 2) {
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
15/06/2030
======== EXPECT
Data invalida.
<<<<<<<< FINISH
```


[Código](./C/draft.c)
