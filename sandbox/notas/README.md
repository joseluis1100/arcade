# Quatro notas, calcule a média

Leia quatro notas, calcule a média aritmética e imprima o resultado.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float nota1, nota2, nota3, nota4;
    scanf("%f %f %f %f", &nota1, &nota2, &nota3, &nota4);

    float media = (nota1 + nota2 + nota3 + nota4) / 4.0;
    
    // O %.Nf , (sendo N um número qualquer) limita a quantidade de casas decimais da variável
    // Ex: %.2f limita a duas casas após a vírgula.
    printf("%.2f\n", media);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
7.0 8.0 9.0 10.0
======== EXPECT
8.50
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0 5.0 5.0 5.0
======== EXPECT
5.00
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0 0.0 0.0 0.0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0 10.0 10.0 10.0
======== EXPECT
10.00
<<<<<<<< FINISH

>>>>>>>> INSERT
3.5 7.2 8.1 6.0
======== EXPECT
6.20
<<<<<<<< FINISH
```

[Código](./C/draft.c)
