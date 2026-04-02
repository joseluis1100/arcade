# Questão 02

Leia um numero fornecido pelo usuário. Se esse número for positivo, calcule a raíz quadrada do numero. Se o numero for negativo, mostre uma mensagem dizendo que o numero e inválido.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#include <math.h>

int main() {
    float numero;
    scanf("%f", &numero);

    // Caso números positivos
    if (numero >= 0) {
        float raiz_quadrada = sqrt(numero);
        printf("%f", raiz_quadrada);
    } else { // Caso números negativos
        printf("Número %f é inválido", numero);
    }

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
25
======== EXPECT
5.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
-4
======== EXPECT
Número -4.000000 é inválido
<<<<<<<< FINISH

>>>>>>>> INSERT
2
======== EXPECT
1.414214
<<<<<<<< FINISH

>>>>>>>> INSERT
100
======== EXPECT
10.000000
<<<<<<<< FINISH
```


[Código](./C/draft.c)
