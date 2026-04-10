# Escrever um programa que leia

Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.  Considere que a cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão abaixo: 

| Especificação | Código | Preço | 
|:---|:---|:---| 
| Cachorro Quente | 100 | 1.20 | 
| Bauru Simples | 101 | 1.30 | 
| Bauru com Ovo | 102 | 1.50 | 
| Hamburguer | 103 | 1.20 | 
| Cheeseburguer | 104 | 1.70 | 
| Suco | 105 | 2.20 | 
| Refrigerante | 106 | 1.00 |

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int codigo, quantidade;
    scanf("%d %d", &codigo, &quantidade);
    if(codigo == 100) {
        printf("%.2f\n", 1.2 * quantidade);
    } else if(codigo == 101) {
        printf("%.2f\n", 1.3 * quantidade);
    } else if(codigo == 102) {
        printf("%.2f\n", 1.5 * quantidade);
    } else if(codigo == 103) {
        printf("%.2f\n", 1.2 * quantidade);
    } else if(codigo == 104) {
    printf("%.2f\n", 1.7 * quantidade);
    } else if(codigo == 105) {
        printf("%.2f\n", 2.2 * quantidade);
    } else if(codigo == 106) {
        printf("%.2f\n", 1 * quantidade);
    }
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
100 2
======== EXPECT
2.40
<<<<<<<< FINISH

>>>>>>>> INSERT
101 3
======== EXPECT
3.90
<<<<<<<< FINISH

>>>>>>>> INSERT
102 1
======== EXPECT
1.50
<<<<<<<< FINISH

>>>>>>>> INSERT
103 5
======== EXPECT
6.00
<<<<<<<< FINISH

>>>>>>>> INSERT
104 2
======== EXPECT
3.40
<<<<<<<< FINISH

>>>>>>>> INSERT
105 1
======== EXPECT
2.20
<<<<<<<< FINISH

>>>>>>>> INSERT
106 4
======== EXPECT
0.00
<<<<<<<< FINISH
```


[Código](./C/draft.c)
