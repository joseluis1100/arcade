# Questão 45

Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASCII para resolver o problema.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    char maiuscula;
    scanf("%c", &maiuscula);

    // Cada caractere é representado por um número inteiro no computador (Tabela ASCII).
    // Perceba que a diferença entre as maiúsculas e minúsculas tem SEMPRE o mesmo valor: 32.
    // A (65) -> a (97) ... 97 - 65 = 32
    // B (66) -> b (98) ... 98 - 66 = 32
    // Então, se somarmos 32 à letra maiúscula, nós avançamos no alfabeto ASCII e caímos na minúscula.
    
    char minuscula = maiuscula + 32;

    printf("%c\n", minuscula);

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
A
======== EXPECT
a
<<<<<<<< FINISH

>>>>>>>> INSERT
Z
======== EXPECT
z
<<<<<<<< FINISH

>>>>>>>> INSERT
B
======== EXPECT
b
<<<<<<<< FINISH

>>>>>>>> INSERT
M
======== EXPECT
m
<<<<<<<< FINISH

>>>>>>>> INSERT
X
======== EXPECT
x
<<<<<<<< FINISH
```

[Código](./C/draft.c)
