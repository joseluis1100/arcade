# Escreva um programa de ajuda

Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

* o total a pagar com desconto de 10%;
* o valor de cada parcela, no parcelamento de 3× sem juros;
* a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
* a comissao do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float valor;
    scanf("%f", &valor);

    // Multiplicar por 0.90 resulta no desconto de 10%
    float valor_desconto10 = valor * 0.90;
    
    // Divisão sempre garantindo que será com decimais
    float valor_parcela = valor / 3.0;

    float comissao_a_vista = valor_desconto10 * 0.05;
    float comissao_parcelada = valor * 0.05;

    // Coloquei um print formatado e dividido em linhas para ficar visualmente elegante pro usuário
    printf("Desconto: %.2f\nParcela: %.2f\nCom. (A Vista): %.2f\nCom. (Prazo): %.2f\n", 
           valor_desconto10, valor_parcela, comissao_a_vista, comissao_parcelada);
    
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
100.0
======== EXPECT
Desconto: 90.00
Parcela: 33.33
Com. (A Vista): 4.50
Com. (Prazo): 5.00
<<<<<<<< FINISH

>>>>>>>> INSERT
200.0
======== EXPECT
Desconto: 180.00
Parcela: 66.67
Com. (A Vista): 9.00
Com. (Prazo): 10.00
<<<<<<<< FINISH

>>>>>>>> INSERT
1000.0
======== EXPECT
Desconto: 900.00
Parcela: 333.33
Com. (A Vista): 45.00
Com. (Prazo): 50.00
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
Desconto: 0.00
Parcela: 0.00
Com. (A Vista): 0.00
Com. (Prazo): 0.00
<<<<<<<< FINISH

>>>>>>>> INSERT
500.0
======== EXPECT
Desconto: 450.00
Parcela: 166.67
Com. (A Vista): 22.50
Com. (Prazo): 25.00
<<<<<<<< FINISH
```

[Código](./C/draft.c)
