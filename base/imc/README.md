# Questão 41

Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo: 

| IMC | Classificação | 
|:---|:---| 
| < 18,5 | Abaixo do Peso | 
| 18,6 - 24,9 | Saudável | 
| 25,0 - 29,9 | Peso em excesso | 
| 30,0 - 34,9 | Obesidade Grau I | 
| 35,0 - 39,9 | Obesidade Grau II(severa) | 
| ≥40,0 | Obesidade Grau III(morbida) |

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float peso, altura;
    scanf("%f %f", &peso, &altura);
    float imc = peso/(altura*altura);
    if(imc >= 40) {
        printf("Obesidade Grau III(morbida)\n");
    } else if(imc >= 35) {
        printf("Obesidade Grau II(severa)\n");
    } else if(imc >= 30) {
        printf("Obesidade Grau I\n");
    } else if(imc >= 25) {
        printf("Peso em excesso\n");
    } else if(imc >= 18.6) {
        printf("Saudável\n");
    } else {
        printf("Abaixo do Peso\n");
    }
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
70.0 1.75
======== EXPECT
Saudável
<<<<<<<< FINISH

>>>>>>>> INSERT
50.0 1.70
======== EXPECT
Abaixo do Peso
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0 1.70
======== EXPECT
Obesidade Grau I
<<<<<<<< FINISH

>>>>>>>> INSERT
120.0 1.60
======== EXPECT
Obesidade Grau III(morbida)
<<<<<<<< FINISH

>>>>>>>> INSERT
150.0 1.50
======== EXPECT
Obesidade Grau III(morbida)
<<<<<<<< FINISH

>>>>>>>> INSERT
80.0 1.80
======== EXPECT
Saudável
<<<<<<<< FINISH
```


[Código](./C/draft.c)
