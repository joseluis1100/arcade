# Valor de comprimento em centímetros

Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas. A formula de conversão é: P = C / 2,54 , sendo C o comprimento em centímetros e P o comprimento em polegadas.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float C;
    scanf("%f", &C);

    float P = C / 2.54;
    printf("%f\n", P);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
2.54
======== EXPECT
1.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
25.4
======== EXPECT
10.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
12.7
======== EXPECT
5.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
30.48
======== EXPECT
12.000000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
