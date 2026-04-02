# Questão 34

Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito. 

| NOTA | CONCEITO (ATÉ 20 FALTAS) | CONCEITO (MAIS DE 20 FALTAS) | 
|:---|:---|:---| 
| 9.0 até 10.0 | A | B | 
| 7.5 até 8.9 | B | C | 
| 5.0 até 7.4 | C | D | 
| 4.0 até 4.9 | D | E | 
| 0.0 até 3.9 | E | E |

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float nota;
    int faltas;
    scanf("%f %d", &nota, &faltas);
    if(faltas > 20) {
        if(nota >= 9) {
            printf("B\n");
        } else if(nota >= 7.5) {
            printf("C\n");
        } else if(nota >= 5) {
            printf("D\n");
        } else {
            printf("E\n");
        }
    } else {
        if(nota >= 9) {
            printf("A\n");
        } else if(nota >= 7.5) {
            printf("B\n");
        } else if(nota >= 5) {
            printf("C\n");
        } else if(nota >= 4) {
            printf("D\n");
        } else {
            printf("E\n");
        }
    }
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
9.5 10
======== EXPECT
A
<<<<<<<< FINISH

>>>>>>>> INSERT
8.0 10
======== EXPECT
B
<<<<<<<< FINISH

>>>>>>>> INSERT
6.0 10
======== EXPECT
C
<<<<<<<< FINISH

>>>>>>>> INSERT
4.5 10
======== EXPECT
D
<<<<<<<< FINISH

>>>>>>>> INSERT
3.0 10
======== EXPECT
E
<<<<<<<< FINISH

>>>>>>>> INSERT
9.5 25
======== EXPECT
B
<<<<<<<< FINISH

>>>>>>>> INSERT
8.0 25
======== EXPECT
C
<<<<<<<< FINISH

>>>>>>>> INSERT
6.0 25
======== EXPECT
D
<<<<<<<< FINISH

>>>>>>>> INSERT
3.0 25
======== EXPECT
E
<<<<<<<< FINISH
```


[Código](./C/draft.c)
