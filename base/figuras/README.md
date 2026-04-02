# Questão 17

Faça um programa que calcule e mostre a area de um trapézio. Sabe-se que: A = (basemaior + basemenor) ∗ altura / 2. Lembre-se a base maior e a base menor devem ser numeros maiores que zero

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float baseMaior, baseMenor, altura;
    scanf("%f %f %f", &baseMaior, &baseMenor, &altura);
    
    if (baseMaior <= 0 || baseMenor <= 0) {
        printf("Base invalida\n");
        // o return 0 é colocado aqui para encerrar o código. Se não ainda seria calculado a area
        return 0;
    }
    
    float area = (baseMaior + baseMenor) * altura / 2;
    printf("%.2f\n", area);
    
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1 5.0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
2 5.0
======== EXPECT
0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
3 5.0 3.0
======== EXPECT
12.00
<<<<<<<< FINISH

>>>>>>>> INSERT
4 5.0 3.0
======== EXPECT
13.50
<<<<<<<< FINISH

>>>>>>>> INSERT
5 5.0
======== EXPECT
0.00
<<<<<<<< FINISH
```


[Código](./C/draft.c)
