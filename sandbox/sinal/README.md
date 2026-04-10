# Ler um numero inteiro. Se

Ler um numero inteiro. Se o numero lido for negativo, escreva a mensagem “Numero invalido”. Se o numero for positivo, calcular o logaritmo deste numero.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
// Usar a biblioteca math para calcular o logarítimo
#include <math.h>

int main() {
    int numero;
    scanf("%d", &numero);
    
    // log(0) não existe, logo tem que ser maior que 0
    if (numero > 0) {
        // logaritimo retorna um double, então basta converter o inteiro
        double logaritmo = log10(numero);
        // para referenciar um double utilize "%lf"
        printf("%lf\n", logaritmo);
    } else {
        printf("Numero invalido");
    }
    
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10
======== EXPECT
1.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
0
======== EXPECT
Numero invalido
<<<<<<<< FINISH

>>>>>>>> INSERT
-5
======== EXPECT
Numero invalido
<<<<<<<< FINISH

>>>>>>>> INSERT
100
======== EXPECT
2.000000
<<<<<<<< FINISH

>>>>>>>> INSERT
1
======== EXPECT
0.000000
<<<<<<<< FINISH
```


[Código](./C/draft.c)
