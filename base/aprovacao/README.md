# Questão 08

Faça um programa que leia 2 notas de um aluno, verifique se as notas sao válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota nao possua um valor válido, este fato deve ser informado ao usuario e o programa termina.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float nota1, nota2;
    scanf("%f %f", &nota1, &nota2);
    
    /* Verificação se as notas são válidas
    
    Busque ter a prática de colocar as expressões entre parênteses para o código ser mais legível e claro, pois primeiro é verificado a nota1 e nota2, para comparar se ambos os valores são verdadeiros, ou seja, as notas são válidas, caso ambas ou apenas uma nota seja inválida, irá para o else.
    
    IMPORTANTE: Quando houver uma mistura de &&(e) e ||(ou) o parêntese é essencial para evitar possíveis erros no compilador, pois && tem maior prioridade do que ||
    */
    if ((nota1 >= 0 && nota1 <= 10) && (nota2 >= 0 && nota2 <= 10)) {
        float media = (nota1 + nota2) / 2;
        printf("%.2f\n", media);
    } else {
        printf("Nota invalida\n");
    }
    
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
7.0 8.0 9.0 10.0
======== EXPECT
7.50
<<<<<<<< FINISH

>>>>>>>> INSERT
3.0 4.0 2.0 1.0
======== EXPECT
3.50
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0 5.0 5.0 5.0
======== EXPECT
5.00
<<<<<<<< FINISH

>>>>>>>> INSERT
10.0 10.0 10.0 10.0
======== EXPECT
10.00
<<<<<<<< FINISH

>>>>>>>> INSERT
6.9 7.0 7.1 6.0
======== EXPECT
6.95
<<<<<<<< FINISH
```


[Código](./C/draft.c)
