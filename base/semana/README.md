# Questão 15

Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int dia;
    scanf("%d", &dia);
    
    // o switch permite que você analise casos quando uma variável tem vários possíveis valores.
    // Ele vai seguir o padrão "switch(variavel) { case valor: }". Onde caso essa varíavel tenha esse valor em específico, o código desse case será executado.
    // ATENÇÃO: no fim de todo código do case, é necessário dar um break; isso sinaliza para o compilador que o switch acaba ali. Se não fizer isso, o compilador irá rodar todos os outros cases, mesmo que o valor não corresponda.
    
    switch (dia) {
    case 1:
        printf("Domingo\n");
        break;
    case 2:
        printf("Segunda\n");
        break;
    case 3:
        printf("Terca\n");
        break;
    case 4:
        printf("Quarta\n");
        break;
    case 5:
        printf("Quinta\n");
        break;
    case 6:
        printf("Sexta\n");
        break;
    case 7:
        printf("Sabado\n");
        break;

    // o default funciona como o else, qualquer caso que não satisfaça algum dos case, se enquadra no default
    default:
        printf("Dia invalido\n");
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
Domingo
<<<<<<<< FINISH

>>>>>>>> INSERT
2
======== EXPECT
Segunda
<<<<<<<< FINISH

>>>>>>>> INSERT
3
======== EXPECT
Terca
<<<<<<<< FINISH

>>>>>>>> INSERT
4
======== EXPECT
Quarta
<<<<<<<< FINISH

>>>>>>>> INSERT
5
======== EXPECT
Quinta
<<<<<<<< FINISH
```


[Código](./C/draft.c)
