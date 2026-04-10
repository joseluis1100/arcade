# Temperatura em graus Celsius

Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = C ∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    //declarado em float para aceitar casas decimais
    float c;
    scanf("%f", &c);
    //colocado "(9.0/5.0)" para indicar valor float, retornando 1.8 ao invés de 1
    float f = c * (9.0/5.0) + 32;
    printf("%f\n", f);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
0.0
======== EXPECT
32.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
212.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
-40.0
======== EXPECT
-40.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
37.0
======== EXPECT
98.599998
<<<<<<<< FINISH

>>>>>>>> INSERT
25.0
======== EXPECT
77.000000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
