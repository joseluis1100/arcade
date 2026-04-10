# Faça um programa para ler

Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int c, l;
    float preco;
    
    scanf("%d %d", &c, &l);
    // ATENÇÃO: a variável 'preco' deve ser lida no float. Antes ela estava como int na declaração!
    scanf("%f", &preco);
    
    // O comprimento total da cerca é igual ao perímetro do terreno
    float perimetro = 2.0 * (c + l);
    float custo = preco * perimetro;

    printf("%.2f\n", custo);

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10 5
3.50
======== EXPECT
105.00
<<<<<<<< FINISH

>>>>>>>> INSERT
20 10
5.00
======== EXPECT
300.00
<<<<<<<< FINISH

>>>>>>>> INSERT
1 1
10.00
======== EXPECT
40.00
<<<<<<<< FINISH

>>>>>>>> INSERT
100 50
2.00
======== EXPECT
600.00
<<<<<<<< FINISH

>>>>>>>> INSERT
30 15
7.25
======== EXPECT
652.50
<<<<<<<< FINISH
```

[Código](./C/draft.c)
