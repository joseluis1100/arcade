# Numero real. Se o numero

Leia um numero real. Se o numero for positivo imprima a raiz quadrada. Do contrário, imprima o numero ao quadrado.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#include <math.h>

int main() {
    float numero;
    scanf("%f", &numero);

    if (numero >= 0) {
        float raiz_quadrada = sqrt(numero);
        printf("%f\n", raiz_quadrada);
    } else {
        float numero_ao_quadrado = pow(numero, 2);
        printf("%f\n", numero_ao_quadrado);
    }

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
4
======== EXPECT
2.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
-9
======== EXPECT
81.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
1
======== EXPECT
1.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
16
======== EXPECT
4.000000
<<<<<<<< FINISH
```


[Código](./C/draft.c)
