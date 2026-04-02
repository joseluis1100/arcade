# Questão 50

Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int idade, anoAtual;
    scanf("%d %d", &idade, &anoAtual);
    //essa questão leva em conta que a pessoa já fez aniversário no ano atual
    int anoNascimento = anoAtual - idade;
    printf("%d\n", anoNascimento);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
25 2024
======== EXPECT
1999
<<<<<<<< FINISH

>>>>>>>> INSERT
0 2024
======== EXPECT
2024
<<<<<<<< FINISH

>>>>>>>> INSERT
30 2000
======== EXPECT
1970
<<<<<<<< FINISH

>>>>>>>> INSERT
18 2025
======== EXPECT
2007
<<<<<<<< FINISH

>>>>>>>> INSERT
50 2024
======== EXPECT
1974
<<<<<<<< FINISH
```

[Código](./C/draft.c)
