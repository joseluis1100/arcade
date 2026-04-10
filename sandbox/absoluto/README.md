# Numero e, caso ele seja

Faça um programa que leia um numero e, caso ele seja positivo, calcule e mostre:
* O numero digitado ao quadrado
* A raiz quadrada do numero digitado

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#include <math.h>

int main() {
    float numero;
    scanf("%f", &numero);

    if (numero >= 0) {
        float numero_ao_quadrado = pow(numero, 2);
        float raiz_quadrada = sqrt(numero);
        printf("%f\n", numero_ao_quadrado);
        printf("%f\n", raiz_quadrada);
    } else {
        printf("Invalido: numero negativo");
    }

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
5
======== EXPECT
25.000000
2.236068
<<<<<<<< FINISH

>>>>>>>> INSERT
-3
======== EXPECT
Invalido: numero negativo
<<<<<<<< FINISH

>>>>>>>> INSERT
0
======== EXPECT
0.000000
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
7
======== EXPECT
49.000000
2.645751
<<<<<<<< FINISH

>>>>>>>> INSERT
10
======== EXPECT
100.000000
3.162278
<<<<<<<< FINISH
```


[Código](./C/draft.c)
