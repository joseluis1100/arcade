# Número inteiro positivo de três

Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos dígitos invertidos do número lido.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int x;
    scanf("%d", &x);
    //usa resto da divisão por 10 para extrair o ultimo dígito
    int d3 = x % 10;
    //a divisão inteira por 10 remove o ultimo dígito, repete o mesmo processo
    int d2 = (x / 10) % 10;
    //a divisão inteira por 100 remove os dois ultimos dígitos, repete o mesmo processo
    int d1 = (x / 100) % 10;
    int numeroInvertido = (d3 * 100) + (d2 * 10) + d1;
    printf("%d\n", numeroInvertido);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
123
======== EXPECT
321
<<<<<<<< FINISH

>>>>>>>> INSERT
456
======== EXPECT
654
<<<<<<<< FINISH

>>>>>>>> INSERT
100
======== EXPECT
1
<<<<<<<< FINISH

>>>>>>>> INSERT
999
======== EXPECT
999
<<<<<<<< FINISH

>>>>>>>> INSERT
501
======== EXPECT
105
<<<<<<<< FINISH
```

[Código](./C/draft.c)
