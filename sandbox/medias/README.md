# Três números inteiros positivos

Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo com um valor numérico digitado pelo usuário: 

(a) Geométrica: ³√(x∗y∗z)​\
(b) Ponderada: (x+2∗y+3∗z)/6\
(c) Harmônica: 1/((1/x)​+(1/y)+(1/z))\
(d) Aritmética: (x+y+z​)/3

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#include <math.h>

int main() {
    int x, y, z;
    float resultado;
    char opcao;
    scanf("%d %d %d %c", &x, &y, &z, &opcao);
    switch(opcao) {
    case 'a':
        // cbrt() faz raiz cubica
        resultado = cbrt(x * y * z);
        break;
    case 'b':
        resultado = (x + 2 * y + 3 * z) / 6.0;
        break;
    case 'c':
        resultado = 1/((1.0/x)+(1.0/y)+(1.0/z));
        break;
    case 'd':
        resultado = (x+y+z)/3.0;
        break;
    default:
        printf("Erro: valor invalido.\n");
        return 1;
    }
    printf("%f\n", resultado);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
2 3 4 a
======== EXPECT
2.884499
<<<<<<<< FINISH

>>>>>>>> INSERT
2 3 4 b
======== EXPECT
3.333333
<<<<<<<< FINISH

>>>>>>>> INSERT
2 3 4 c
======== EXPECT
0.923077
<<<<<<<< FINISH

>>>>>>>> INSERT
2 3 4 d
======== EXPECT
3.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
2 3 4 e
======== EXPECT
Erro: valor invalido.
<<<<<<<< FINISH
```


[Código](./C/draft.c)
