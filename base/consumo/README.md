# Questão 26

Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo: 

| CONSUMO | (Km/l) | MENSAGEM | 
|:---|:---|:---| 
| menor que | 8 | Venda o carro! | 
| entre | 8 e 14 | Econômico! | 
| maior que | 14 | Super econômico! |

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float km, litros;
    scanf("%f %f", &km, &litros);
    float kmporl = km / litros;
    if(kmporl < 8) {
        printf("Venda o carro!");
    } else if(kmporl <= 14) { // o if anterior retira a necessidade de especificar ser maior que 8
        printf("Economico!");
    } else {
        printf("Super economico!");
    }
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
100.0 20.0
======== EXPECT
Venda o carro!
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0 8.0
======== EXPECT
Economico!
<<<<<<<< FINISH

>>>>>>>> INSERT
100.0 5.0
======== EXPECT
Super economico!
<<<<<<<< FINISH

>>>>>>>> INSERT
500.0 40.0
======== EXPECT
Economico!
<<<<<<<< FINISH

>>>>>>>> INSERT
200.0 15.0
======== EXPECT
Economico!
<<<<<<<< FINISH
```


[Código](./C/draft.c)
