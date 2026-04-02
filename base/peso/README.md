# Questão 10

Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde a altura): 
* Homens: (72.7 ∗ h) − 58
* Mulheres: (62.1 ∗ h) − 44.7

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float h;
    // char armazena apenas um "caractere"
    char sexo;
    scanf("%f %c", &h, &sexo);
    
    // usamos aspas simples para referenciar um caractere
    if (sexo == 'h') {
        float homem = (72.7 * h) - 58;
        printf("%f\n", homem);
    } else if (sexo == 'm') {
        float mulher = (62.1 * h) - 44.7;
        printf("%f\n", mulher);
    }
    // detalhe importante. 'M' é um caractere diferente de 'm', então cuidado para não confundir e fazer uma comparação errada
    
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1.80 h
======== EXPECT
72.859993
<<<<<<<< FINISH

>>>>>>>> INSERT
1.65 m
======== EXPECT
57.764999
<<<<<<<< FINISH

```


[Código](./C/draft.c)
