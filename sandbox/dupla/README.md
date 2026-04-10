# Faça um algoritmo que calcule

Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno é indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int n1, n2, n3;
    scanf("%d %d %d", &n1, &n2, &n3);
    
    // a média ponderada é a soma das multiplicações da nota pelo seu respectivo peso, dividido pela soma dos pesos
    float media_pon = ((n1 * 1) + (n2 * 1) + (n3 * 2)) / 4.0;
    if (media_pon >= 60) {
        printf("Aprovado\n");
    } else {
        printf("Reprovado\n");
    }
    
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
8.0 9.0
======== EXPECT
Reprovado
<<<<<<<< FINISH

>>>>>>>> INSERT
4.0 3.0
======== EXPECT
Reprovado
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0 5.0
======== EXPECT
Reprovado
<<<<<<<< FINISH

>>>>>>>> INSERT
7.0 6.0
======== EXPECT
Reprovado
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0 10.0
======== EXPECT
Reprovado
<<<<<<<< FINISH
```


[Código](./C/draft.c)
