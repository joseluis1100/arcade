# Valor de um produto

Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float valor_produto;
    scanf("%f", &valor_produto);

    // 100% - 12% = 88% (0.88). 
    // É uma forma mais rápida e limpa de calcular!
    float valor_com_desconto = valor_produto * 0.88;

    printf("%.2f\n", valor_com_desconto);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
100.0 10.0
======== EXPECT
88.00
<<<<<<<< FINISH

>>>>>>>> INSERT
200.0 5.0
======== EXPECT
176.00
<<<<<<<< FINISH

>>>>>>>> INSERT
50.0 0.0
======== EXPECT
44.00
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0 50.0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
1000.0 15.0
======== EXPECT
880.00
<<<<<<<< FINISH
```

[Código](./C/draft.c)
