# Questão 36

Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = π ∗ raio² ∗ altura, onde π = 3.141592.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#include <math.h>
#define PI 3.141592

int main() {
    float altura, raio;
    scanf("%f %f", &altura, &raio);
    float volume = PI * pow(raio, 2) * altura;
    printf("%f\n", volume);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.0 1.0
======== EXPECT
3.141592
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0 10.0
======== EXPECT
1570.796021
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0 0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
2.5 3.0
======== EXPECT
70.685822
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0 5.0
======== EXPECT
785.398010
<<<<<<<< FINISH
```

[Código](./C/draft.c)
