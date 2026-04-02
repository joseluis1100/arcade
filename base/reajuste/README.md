# Questão 38

Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float salario;
    scanf("%f", &salario);
    //125% = valor * 1.25
    float novoSalario = salario * 1.25;
    printf("%.2f\n", novoSalario);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1000.0
======== EXPECT
1250.00
<<<<<<<< FINISH

>>>>>>>> INSERT
2500.0
======== EXPECT
3125.00
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
500.0
======== EXPECT
625.00
<<<<<<<< FINISH

>>>>>>>> INSERT
10000.0
======== EXPECT
12500.00
<<<<<<<< FINISH
```

[Código](./C/draft.c)
