# Questão 34

Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área do círculo é π ∗ raio², considere π = 3.141592.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#include <math.h>
#define PI 3.141592

int main() {
    float raio;
    scanf("%f", &raio);
    float area = PI * pow(raio, 2);
    printf("%f\n", area);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.0
======== EXPECT
3.141592
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0
======== EXPECT
78.539803
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
314.159210
<<<<<<<< FINISH

>>>>>>>> INSERT
2.5
======== EXPECT
19.634951
<<<<<<<< FINISH
```

[Código](./C/draft.c)
