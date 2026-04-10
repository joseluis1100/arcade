# Salário-base de um funcionário. Calcule

Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float salarioBase;
    scanf("%f", &salarioBase);
    //100% + 5% - 7% = 98% = 0.98
    float salario = salarioBase * 0.98;
    printf("%.2f\n", salario);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1000.0
======== EXPECT
980.00
<<<<<<<< FINISH

>>>>>>>> INSERT
2500.0
======== EXPECT
2450.00
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
500.0
======== EXPECT
490.00
<<<<<<<< FINISH

>>>>>>>> INSERT
10000.0
======== EXPECT
9800.00
<<<<<<<< FINISH
```

[Código](./C/draft.c)
