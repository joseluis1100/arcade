# Questão 30

Faça um programa que receba três números e mostre-os em ordem crescente.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    // primeiro descobrimos qual o menor, depois verificamos meio e final
    if(a < b && a < c) {
        if(b < c) {
            printf("%d %d %d\n", a, b, c);
        } else {
            printf("%d %d %d\n", a, c, b);
        }
    } else if(b < a && b < c) {
        if(a < c) {
            printf("%d %d %d\n", b, a, c);
        } else {
            printf("%d %d %d\n", b, c, a);
        }
    } else {
        if(a < b) {
            printf("%d %d %d\n", c, a, b);
        } else {
            printf("%d %d %d\n", c, b, a);
        }
    }
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
3 1 2
======== EXPECT
1 2 3
<<<<<<<< FINISH

>>>>>>>> INSERT
1 2 3
======== EXPECT
1 2 3
<<<<<<<< FINISH

>>>>>>>> INSERT
3 2 1
======== EXPECT
1 2 3
<<<<<<<< FINISH

>>>>>>>> INSERT
5 5 5
======== EXPECT
5 5 5
<<<<<<<< FINISH

>>>>>>>> INSERT
1 3 2
======== EXPECT
1 2 3
<<<<<<<< FINISH
```


[Código](./C/draft.c)
