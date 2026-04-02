# Questão 20

Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se e um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
* O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
* Chama-se equilatero o triângulo que tem três lados iguais.
* Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
* Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);
    
    // Verificação se é válido ser um triângulo
    if ((a+b > c) && (a+c > b) && (b+c > a)) {
        
        // se a = b e a = c, então b = c
        if ((a == b && a == c)) {
            printf("equilátero\n");
            return 0;

        // a ser diferente de b e de c, não faz necessariamente b ser diferente de c. Então precisamos abranger todos os casos
        } else if (a != b && a != c && b != c) {
            printf("escaleno\n");
            return 0;
        } else {
            printf("isósceles\n");
        }
    } else {
        printf("inválido\n");
    }
    
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
3.0 4.0 5.0
======== EXPECT
escaleno
<<<<<<<< FINISH

>>>>>>>> INSERT
5.0 5.0 5.0
======== EXPECT
equilátero
<<<<<<<< FINISH

>>>>>>>> INSERT
3.0 3.0 5.0
======== EXPECT
isósceles
<<<<<<<< FINISH

>>>>>>>> INSERT
1.0 2.0 10.0
======== EXPECT
inválido
<<<<<<<< FINISH

>>>>>>>> INSERT
7.0 7.0 7.0
======== EXPECT
equilátero
<<<<<<<< FINISH
```


[Código](./C/draft.c)
