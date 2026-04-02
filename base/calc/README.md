# Questão 18

Faça um programa que mostre ao usuario um menu com 4 opções de operações matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    printf("Escolha o número referente a operação que deseja utilizar:\n");
    printf("1. +\n");
    printf("2. -\n");
    printf("3. *\n");
    printf("4. /\n");
    
    int operador;
    scanf("%d", &operador);
    printf("Digite dois valores:\n");
    
    float n1, n2;
    scanf("%f %f", &n1, &n2);
    
    float resultado;
    switch (operador) {
    case 1:
        resultado = n1 + n2;
        printf("Soma = %f", resultado);
        break;
        
    case 2:
        resultado = n1 - n2;
        printf("Subtração = %f", resultado);
        break;
        
    case 3: 
        resultado = n1 * n2;
        printf("Multiplicação = %f", resultado);
        break;
        
    default:
        resultado = n1 / n2;
        printf("Divisão = %f", resultado);
        break;
    }
    
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1
5 3
======== EXPECT
Escolha o número referente a operação que deseja utilizar:
1. +
2. -
3. *
4. /
Digite dois valores:
Soma = 8.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
2
10 4
======== EXPECT
Escolha o número referente a operação que deseja utilizar:
1. +
2. -
3. *
4. /
Digite dois valores:
Subtração = 6.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
3
6 3
======== EXPECT
Escolha o número referente a operação que deseja utilizar:
1. +
2. -
3. *
4. /
Digite dois valores:
Multiplicação = 18.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
4
8 2
======== EXPECT
Escolha o número referente a operação que deseja utilizar:
1. +
2. -
3. *
4. /
Digite dois valores:
Divisão = 4.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
5
======== EXPECT
Escolha o número referente a operação que deseja utilizar:
1. +
2. -
3. *
4. /
Digite dois valores:
Divisão = -nan
<<<<<<<< FINISH
```


[Código](./C/draft.c)
