# Questão 01

Faça um programa que receba dois numeros e mostre qual deles é o maior.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int n1, n2;
    scanf("%d %d", &n1, &n2);

    /*
    Um "if(){}" é um comando de condicionalidade, onde irá verificar se a expressão dentro do parênteses é verdadeira, caso a expressão seja verdadeira irá realizar o código dentro do escopo "{}", caso seja falsa, o código dentro do "else{}" será executado
    */
    int maior;
    if (n1 > n2) {
        maior = n1;
        printf("%d", maior);
    } else {
        // nesse else em específico, está os casos de (n1 > n2) e (n1 = n2)
        maior = n2;
        printf("%d", maior);
    }

    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
5 3
======== EXPECT
5
<<<<<<<< FINISH

>>>>>>>> INSERT
3 5
======== EXPECT
5
<<<<<<<< FINISH

>>>>>>>> INSERT
5 5
======== EXPECT
5
<<<<<<<< FINISH

>>>>>>>> INSERT
-1 -5
======== EXPECT
-1
<<<<<<<< FINISH

>>>>>>>> INSERT
0 0
======== EXPECT
0
<<<<<<<< FINISH
```


[Código](./C/draft.c)
