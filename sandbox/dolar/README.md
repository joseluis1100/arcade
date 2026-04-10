# Valor em real e a

Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float reais, cotacao;
    scanf("%f %f", &reais, &cotacao);
    float dolar = reais / cotacao;
    printf("%.2f\n", dolar);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
100.0 5.0
======== EXPECT
20.00
<<<<<<<< FINISH

>>>>>>>> INSERT
50.0 4.50
======== EXPECT
11.11
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0 5.0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
1000.0 5.25
======== EXPECT
190.48
<<<<<<<< FINISH

>>>>>>>> INSERT
250.0 3.80
======== EXPECT
65.79
<<<<<<<< FINISH
```

[Código](./C/draft.c)
