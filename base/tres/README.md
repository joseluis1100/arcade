# Questão 03

Peça ao usuário para digitar três valores inteiros e imprima a soma deles.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    //variáveis de mesmo tipo podem ser declaradas na mesma linha
    int valor1, valor2, valor3;
    //scanf de multiplas variáveis pode ser feito assim
    scanf("%d %d %d", &valor1, &valor2, &valor3);
    //é possível iniciar uma variável com um valor
    int soma = valor1 + valor2 + valor3;
    printf("%d\n", soma);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1 2 3
======== EXPECT
6
<<<<<<<< FINISH

>>>>>>>> INSERT
10 20 30
======== EXPECT
60
<<<<<<<< FINISH

>>>>>>>> INSERT
0 0 0
======== EXPECT
0
<<<<<<<< FINISH

>>>>>>>> INSERT
-5 10 -3
======== EXPECT
2
<<<<<<<< FINISH

>>>>>>>> INSERT
100 200 300
======== EXPECT
600
<<<<<<<< FINISH
```

[Código](./C/draft.c)
