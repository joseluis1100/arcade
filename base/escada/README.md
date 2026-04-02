# Questão 44

Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
//iremos usar o math.h para usar uma função de arredondamento
#include <math.h>

int main() {
    float alturaDegrau, objetivo;
    scanf("%f %f", &alturaDegrau, &objetivo);
    //caso o numero dê quebrado, o ceil arredondará para cima, sempre 
    //retornando a quantidade mínima para chegar no objetivo.
    int qtdDegraus = ceil(objetivo / alturaDegrau);
    printf("%d\n", qtdDegraus);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
0.5 2.5
======== EXPECT
5
<<<<<<<< FINISH

>>>>>>>> INSERT
0.3 1.0
======== EXPECT
4
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0 10.0
======== EXPECT
10
<<<<<<<< FINISH

>>>>>>>> INSERT
0.25 1.0
======== EXPECT
4
<<<<<<<< FINISH

>>>>>>>> INSERT
0.15 3.0
======== EXPECT
20
<<<<<<<< FINISH
```

[Código](./C/draft.c)
