# Importância de R$ 780.000,00 será

A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:

* O primeiro ganhador recebera 46%;
* O segundo recebera 32%;
* O terceiro recebera o restante;

### Calcule e imprima a quantia ganha por cada um dos ganhadores.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    // É recomendado usar uma variável 'premio' (float premio = 780000.00;) 
    // para não ter que repetir o mesmo número mágico 3 vezes!
    float primeiro = 780000.00 * 0.46;
    float segundo = 780000.00 * 0.32;
    float terceiro = 780000.00 - (primeiro + segundo);

    printf("1º Ganhador: R$ %.2f\n", primeiro);
    printf("2º Ganhador: R$ %.2f\n", segundo);
    printf("3º Ganhador: R$ %.2f\n", terceiro);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
1000.0
======== EXPECT
1º Ganhador: R$ 358800.00
2º Ganhador: R$ 249600.00
3º Ganhador: R$ 171600.00
<<<<<<<< FINISH

>>>>>>>> INSERT
5000.0
======== EXPECT
1º Ganhador: R$ 358800.00
2º Ganhador: R$ 249600.00
3º Ganhador: R$ 171600.00
<<<<<<<< FINISH

>>>>>>>> INSERT
0.0
======== EXPECT
1º Ganhador: R$ 358800.00
2º Ganhador: R$ 249600.00
3º Ganhador: R$ 171600.00
<<<<<<<< FINISH

>>>>>>>> INSERT
250.0
======== EXPECT
1º Ganhador: R$ 358800.00
2º Ganhador: R$ 249600.00
3º Ganhador: R$ 171600.00
<<<<<<<< FINISH

>>>>>>>> INSERT
10000.0
======== EXPECT
1º Ganhador: R$ 358800.00
2º Ganhador: R$ 249600.00
3º Ganhador: R$ 171600.00
<<<<<<<< FINISH
```

[Código](./C/draft.c)
