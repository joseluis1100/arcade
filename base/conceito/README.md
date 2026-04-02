# Questão 14

A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0 ate 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A media das três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno esta reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float n1, n2, n3;
    scanf("%f %f %f", &n1, &n2, &n3);
    
    float notaFinal = ((n1*2) + (n2*3) + (n3*5)) / (2+3+5);
    if (notaFinal >= 5 && notaFinal <= 10) {
        printf("Aprovado\n");
    } else if (notaFinal >= 3 && notaFinal < 5) {
        printf("Recuperacao\n");
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
8.0 9.0 7.0
======== EXPECT
Aprovado
<<<<<<<< FINISH

>>>>>>>> INSERT
3.0 4.0 2.0
======== EXPECT
Reprovado
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0 6.0 4.0
======== EXPECT
Recuperacao
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0 10.0 10.0
======== EXPECT
Aprovado
<<<<<<<< FINISH

>>>>>>>> INSERT
7.0 7.0 7.0
======== EXPECT
Aprovado
<<<<<<<< FINISH
```


[Código](./C/draft.c)
