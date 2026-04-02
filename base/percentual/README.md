# Questão 09

Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrario imprima: Empréstimo concedido.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float salario, parcela_emprestimo;
    scanf("%f %f", &salario, &parcela_emprestimo);
    
    float parte_do_salario = salario * 0.20;
    
    if (parcela_emprestimo > parte_do_salario) {
        printf("Emprestimo nao concedido\n");
    } else {
        printf("Emprestimo concedido\n");
    }
    
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1000.0 10
======== EXPECT
Emprestimo concedido
<<<<<<<< FINISH

>>>>>>>> INSERT
2000.0 5
======== EXPECT
Emprestimo concedido
<<<<<<<< FINISH

>>>>>>>> INSERT
500.0 20
======== EXPECT
Emprestimo concedido
<<<<<<<< FINISH

>>>>>>>> INSERT
3000.0 0
======== EXPECT
Emprestimo concedido
<<<<<<<< FINISH

>>>>>>>> INSERT
1500.0 15
======== EXPECT
Emprestimo concedido
<<<<<<<< FINISH
```


[Código](./C/draft.c)
