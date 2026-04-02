# Questão 11

Escreva um programa que leia um numero inteiro maior do que zero e com 3 dígitos e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao numero 251 corresponderá o valor 8 (2 + 5 + 1). Se o numero lido não for maior do que zero, o programa terminará com a mensagem “Numero inválido”.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int numero;
    scanf("%d", &numero);
    
    if (numero > 0) {
        // Unidade é o resto do número ao ser dividido por 10
        int unidade = numero % 10;
        // Dividindo um número inteiro por 10, removemos a unidade, e pegamos o resto do número ao ser divido por 10
        int dezena = numero / 10 % 10;
        // Dividindo um número inteiro por 100, removemos a unidade e dezena, sobrando apenas a centena
        int centena = numero / 100;
        
        int soma = unidade + dezena + centena;
        printf("%d\n", soma);
    } else {
        printf("Numero invalido\n");
    }
    
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
5 3
======== EXPECT
5
<<<<<<<< FINISH

>>>>>>>> INSERT
3 8
======== EXPECT
3
<<<<<<<< FINISH

>>>>>>>> INSERT
7 7
======== EXPECT
7
<<<<<<<< FINISH

>>>>>>>> INSERT
-1 -5
======== EXPECT
Numero invalido
<<<<<<<< FINISH

>>>>>>>> INSERT
0 100
======== EXPECT
Numero invalido
<<<<<<<< FINISH
```


[Código](./C/draft.c)
