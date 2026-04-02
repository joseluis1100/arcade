# Questão 21

Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de conversão é: K = L ∗ 0.45 , sendo K a massa em quilogramas e L a massa em libras

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float L;
    scanf("%f", &L);

    float K = L * 0.45;
    printf("%f\n", K);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.0
======== EXPECT
0.450000
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0
======== EXPECT
4.500000
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
2.22
======== EXPECT
0.999000
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0
======== EXPECT
45.000000
<<<<<<<< FINISH
```

[Código](./C/draft.c)
