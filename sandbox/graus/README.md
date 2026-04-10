# Ângulo em graus

Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G ∗ π/180, sendo G o ângulo em graus e R em radianos e π = 3.14.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
//OPCIONAL: usamos o define para criar um "simbolo" para um valor 
//específico. Ele não funciona como uma variável, não pode ser mudado e 
//não gasta espaço na memória.
#define PI 3.14159

int main() {
    float g;
    scanf("%f", &g);
    float r = g * PI / 180;
    printf("%f\n", r);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
180.0
======== EXPECT
3.141590
<<<<<<<< FINISH

>>>>>>>> INSERT
90.0
======== EXPECT
1.570795
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
45.0
======== EXPECT
0.785398
<<<<<<<< FINISH

>>>>>>>> INSERT
360.0
======== EXPECT
6.283180
<<<<<<<< FINISH
```

[Código](./C/draft.c)
