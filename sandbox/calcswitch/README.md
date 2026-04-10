# Escreva o menu de opções

Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.
Escolha a opção:
1. Soma de 2 números.
2. Diferença entre 2 números (maior pelo menor).
3. Produto entre 2 números.
4. Divisão entre 2 números (o denominador não pode ser zero).

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int opcao, x1, x2, resultado;
    scanf("%d", &opcao);
    if(opcao > 4 || opcao < 1) {
        printf("Erro: valor invalido.\n");
        // retorno de erro
        return 1;
    }
    scanf("%d %d", &x1, &x2);
    switch(opcao) {
    case 1:
        resultado = x1 + x2;
        break;
    case 2:
        // nesse caso e na divisão a ordem importa
        if(x1 > x2) {
            resultado = x1 - x2;
        } else {
            resultado = x2 - x1;
        }
        break;
    case 3:
        resultado = x1 * x2;
        break;
    case 4:
        if(x1 > x2) {
            resultado = x1 / x2;
        } else {
            resultado = x2 / x1;
        }
        break;
    }
    printf("%d\n", resultado);
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
8
<<<<<<<< FINISH

>>>>>>>> INSERT
2
10 4
======== EXPECT
6
<<<<<<<< FINISH

>>>>>>>> INSERT
3
6 3
======== EXPECT
18
<<<<<<<< FINISH

>>>>>>>> INSERT
4
8 2
======== EXPECT
4
<<<<<<<< FINISH

>>>>>>>> INSERT
5
======== EXPECT
Erro: valor invalido.
<<<<<<<< FINISH
```


[Código](./C/draft.c)
