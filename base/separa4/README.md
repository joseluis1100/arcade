# Questão 47

Leia um numero inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int numero;
    scanf("%d", &numero);

    // Divisão inteira retira dígitos do final e não preserva decimais
    int milhar = numero / 1000;

    // EX centena: 7591 / 100 = 75 ... 75 % 10 = 5
    int centena = (numero / 100) % 10;

    // EX dezena: 8015 / 10 = 801 ... 801 % 10 = 1
    int dezena = (numero / 10) % 10;

    // EX unidade: 2058 % 10 = 8
    int unidade = numero % 10;

    // Note a quebra de linha (\n) após cada variável para atender a exigência da questão
    printf("%d\n%d\n%d\n%d\n", milhar, centena, dezena, unidade);

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1234
======== EXPECT
1
2
3
4
<<<<<<<< FINISH

>>>>>>>> INSERT
5678
======== EXPECT
5
6
7
8
<<<<<<<< FINISH

>>>>>>>> INSERT
1000
======== EXPECT
1
0
0
0
<<<<<<<< FINISH

>>>>>>>> INSERT
9999
======== EXPECT
9
9
9
9
<<<<<<<< FINISH

>>>>>>>> INSERT
4321
======== EXPECT
4
3
2
1
<<<<<<<< FINISH
```

[Código](./C/draft.c)
