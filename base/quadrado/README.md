# Questão 04

Leia um número real e imprima o resultado do quadrado desse número.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
//OPCIONAL: importar biblioteca math.h para usar a função de potencia
#include <math.h>

int main() {
    float x;
    scanf("%f", &x);
    //pow exige 2 parâmetros, base e expoente
    float quadrado = pow(x, 2);
    printf("%f\n", quadrado);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
3.0
======== EXPECT
9.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
-2.0
======== EXPECT
4.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
10.5
======== EXPECT
110.250000
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0
======== EXPECT
1.000000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
