# Questão 51

Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0, 0).

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#include <math.h>

int main() {
    float x, y;
    scanf("%f %f", &x, &y);

    // A distância da origem se resolve usando o famoso Teorema de Pitágoras! 
    // Onde 'x' e 'y' são os catetos e a distância é a hipotenusa
    float distancia = sqrt(pow(x, 2) + pow(y, 2));

    printf("%.2f\n", distancia);

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
3.0 4.0
======== EXPECT
5.00
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0 0.0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0 0.0
======== EXPECT
1.00
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0 5.0
======== EXPECT
7.07
<<<<<<<< FINISH

>>>>>>>> INSERT
-3.0 4.0
======== EXPECT
5.00
<<<<<<<< FINISH
```

[Código](./C/draft.c)
