# Empresa decide dar um aumento

Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente maior do que os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional de salário. Faça um programa que leia: 

* o valor do salário atual do funcionário; 
* o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa). 

### Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento. 
| Salário Atual | Reajuste(%) | Tempo de Serviço | Bônus | 
|:---|:---|:---|:---| 
| Até 500,00 | 25% | Abaixo de 1 ano | Sem bônus | 
| Até 1000,00 | 20% | De 1 a 3 anos | 100,00 | 
| Até 1500,00 | 15% | De 4 a 6 anos | 200,00 | 
| Até 2000,00 | 10% | De 7 a 10 anos | 300,00 | 
| Acima de 2000,00 | Sem reajuste | Mais de 10 anos | 500,00 |

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float salario;
    int tempoServico;
    scanf("%f %d", &salario, &tempoServico);
    if(salario > 2000) {
        printf("Sem reajuste\n");
    } else if(salario > 1500) {
        salario *= 1.1;
    } else if(salario > 1000) {
        salario *= 1.15;
    } else if(salario > 500) {
        salario *= 1.2;
    } else {
        salario *= 1.25;
    }
    if(tempoServico > 10) {
        salario += 500;
    } else if(tempoServico >= 7) {
        salario += 300;
    } else if(tempoServico >= 4) {
        salario += 200;
    } else if(tempoServico >= 1) {
        salario += 100;
    } else {
        printf("Sem bonus\n");
    }
    printf("%f\n", salario);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1000.0 5
======== EXPECT
1400.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
500.0 11
======== EXPECT
1125.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
2500.0 3
======== EXPECT
Sem reajuste
2600.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
800.0 8
======== EXPECT
1260.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
400.0 0
======== EXPECT
Sem bonus
500.000000
<<<<<<<< FINISH
```


[Código](./C/draft.c)
