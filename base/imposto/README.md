# Questão 24

Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
MG = 1 SP = 2 RJ = 3 MS = 4

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int estado;
    float valor, resultado;
    scanf("%d", &estado);
    if(estado > 4 || estado < 1) {
        printf("Erro: valor invalido.\n");
        return 1;
    }
    scanf("%f", &valor);
    switch(estado) {
    case 1:
        resultado = valor * 1.07;
        break;
    case 2:
        resultado = valor * 1.12;
        break;
    case 3:
        resultado = valor * 1.15;
        break;
    case 4:
        resultado = valor * 1.08;
        break;
    }
    printf("%.2f\n", resultado);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1
100.0
======== EXPECT
107.00
<<<<<<<< FINISH

>>>>>>>> INSERT
2
100.0
======== EXPECT
112.00
<<<<<<<< FINISH

>>>>>>>> INSERT
3
100.0
======== EXPECT
115.00
<<<<<<<< FINISH

>>>>>>>> INSERT
4
100.0
======== EXPECT
108.00
<<<<<<<< FINISH

>>>>>>>> INSERT
5
======== EXPECT
Erro: valor invalido.
<<<<<<<< FINISH
```


[Código](./C/draft.c)
