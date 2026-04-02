# Questão 25

Calcule as raízes da equação de 2o grau. Lembrando que:
x = (−b ± √∆) / (2a)\
Onde:\
∆ = B² − 4ac\
E ax² + bx + c = 0 representa uma equação de 2o grau.\
A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem “Não é equação de segundo grau”.
* Se ∆ < 0, não existe real. Imprima a mensagem Não existe raiz.
* Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única.
* Se ∆ ≥ 0, imprima as duas raízes reais.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#include <math.h>

int main() {
    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);
    if(a == 0) {
        printf("Nao eh equacao de segundo grau\n");
        return 1;
    }
    float delta = pow(b, 2) - 4 * a * c;
    if(delta < 0) {
        printf("Nao existe raiz.\n");
    } else if(delta == 0) {
        // se delta é 0, não é necessário
        float x = -b / (2 * a);
        printf("%f\nRaiz unica.\n", x);
    } else {
        float x1 = (-b + sqrt(delta)) / (2 * a);
        float x2 = (-b - sqrt(delta)) / (2 * a);
        printf("%f %f\n", x1, x2);
    }
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.0 -5.0 6.0
======== EXPECT
3.000000 2.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0 -2.0 1.0
======== EXPECT
1.000000
Raiz unica.
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0 1.0 1.0
======== EXPECT
Nao existe raiz.
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0 5.0 3.0
======== EXPECT
Nao eh equacao de segundo grau
<<<<<<<< FINISH

>>>>>>>> INSERT
2.0 -8.0 6.0
======== EXPECT
3.000000 1.000000
<<<<<<<< FINISH
```


[Código](./C/draft.c)
