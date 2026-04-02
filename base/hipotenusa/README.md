# Questão 35

Sejam a e b os catetos de um triângulo, onde a hipotênusa é obtida pela equação: hipotenusa = √a² + b². Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
#include <math.h>

int main() {
    float a, b;
    scanf("%f %f", &a, &b);

    // sqrt() é usada para calcular raiz quadrada, está presente na biblioteca <math.h>
    // float hipotenusa = sqrt( pow(a, 2) + pow(b, 2) );
    
    // Simplificando sem usar o pow: (lembrando que a multiplicação tem prioridade sobre a soma)
    float hipotenusa = sqrt(a * a + b * b);

    printf("%.2f\n", hipotenusa);
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
5.0 12.0
======== EXPECT
13.00
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0 0.0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0 1.0
======== EXPECT
1.41
<<<<<<<< FINISH

>>>>>>>> INSERT
8.0 15.0
======== EXPECT
17.00
<<<<<<<< FINISH
```

[Código](./C/draft.c)
