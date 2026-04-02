# Questão 37

As tarifas de certo parque de estacionamento são as seguintes: 

* 1a e 2a hora R$ 1,00 cada 
* 3a e 4a hora R$ 1,40 cada 
* 5a hora e seguintes R$ 2,00 cada 

### O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida deste são apresentados na forma de pares de inteiros, representando horas e minutos. Por exemplo, o par 12 50 representará "dez para a uma da tarde". Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int horaEntrada, minutoEntrada, horaSaida, minutoSaida;
    float valor;
    scanf("%d %d %d %d", &horaEntrada, &minutoEntrada, &horaSaida, &minutoSaida);
    // Transformamos tudo em minutos para evitar erros na virada do dia
    int tempoEntrada = horaEntrada * 60 + minutoEntrada;
    int tempoSaida = horaSaida * 60 + minutoSaida;
    // Se o momento de saída for antes ou igual ao de entrada, 
    // significa que passou para o dia seguinte
    if (tempoSaida <= tempoEntrada) {
        tempoSaida += 24 * 60;
    }
    int diferenca = tempoSaida - tempoEntrada;
    // se for divisível por 60, não há minutos sobrando, se não, soma 1 hora
    if(diferenca % 60 == 0) {
        diferenca /= 60;
    } else {
        diferenca = diferenca / 60 + 1;
    }
    if(diferenca >= 5) {
        valor = 4.8 + 2 * (diferenca - 4);
    } else if(diferenca == 4) {
        valor = 4.8;
    } else if(diferenca == 3) {
        valor = 3.4;
    } else if(diferenca == 2) {
        valor = 2;
    } else if(diferenca == 1) {
        valor = 1;
    }
    printf("%.2f\n", valor);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
8 0 9 0
======== EXPECT
1.00
<<<<<<<< FINISH

>>>>>>>> INSERT
10 30 12 0
======== EXPECT
2.00
<<<<<<<< FINISH

>>>>>>>> INSERT
14 0 18 30
======== EXPECT
6.80
<<<<<<<< FINISH

>>>>>>>> INSERT
22 0 2 0
======== EXPECT
4.80
<<<<<<<< FINISH

>>>>>>>> INSERT
8 0 8 30
======== EXPECT
1.00
<<<<<<<< FINISH
```


[Código](./C/draft.c)
