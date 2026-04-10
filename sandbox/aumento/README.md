# Produto vai sofrer aumento de

Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela). 

| PREÇO ANTIGO | PERCENTUAL DE AUMENTO | 
|:---|:---| 
| até R$ 50 | 5% | 
| entre R$ 50 e R$ 100 | 10% | 
| acima de R$ 100 | 15% | 

| PREÇO NOVO | MENSAGEM | 
|:---|:---| 
| até R$ 80 | Barato | 
| entre R$ 80 e R$ 120 (inclusive) | Normal | 
| entre R$ 120 e R$ 200 (inclusive) | Caro | 
| acima de R$ 200 | Muito caro |

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    float preco;
    scanf("%f", &preco);
    if(preco > 100) {
        preco *= 1.15;
    } else if(preco > 50) {
        preco *= 1.1;
    } else {
        preco *= 1.05;
    }
    // após o aumento vem a verificação
    if(preco > 200) {
        printf("Muito caro\n");
    } else if(preco > 120) {
        printf("Caro\n");
    } else if(preco > 80) {
        printf("Normal\n");
    } else {
        printf("Barato\n");
    }
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
150.0
======== EXPECT
Caro
<<<<<<<< FINISH

>>>>>>>> INSERT
80.0
======== EXPECT
Normal
<<<<<<<< FINISH

>>>>>>>> INSERT
30.0
======== EXPECT
Barato
<<<<<<<< FINISH

>>>>>>>> INSERT
200.0
======== EXPECT
Muito caro
<<<<<<<< FINISH

>>>>>>>> INSERT
50.0
======== EXPECT
Barato
<<<<<<<< FINISH
```


[Código](./C/draft.c)
