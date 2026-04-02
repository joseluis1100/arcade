# Questão 22

Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são
* Ter pelo menos 65 anos,
* Ou ter trabalhado pelo menos 30 anos,
* Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>

int main() {
    int idade, tempoServico;
    scanf("%d %d", &idade, &tempoServico);
    if(idade >= 65 || tempoServico >= 30 || (idade >= 60 && tempoServico >= 25)) {
        printf("Pode se aposentar\n");
    } else {
        printf("Nao pode se aposentar\n");
    }
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
65 20
======== EXPECT
Pode se aposentar
<<<<<<<< FINISH

>>>>>>>> INSERT
50 30
======== EXPECT
Pode se aposentar
<<<<<<<< FINISH

>>>>>>>> INSERT
60 25
======== EXPECT
Pode se aposentar
<<<<<<<< FINISH

>>>>>>>> INSERT
30 10
======== EXPECT
Nao pode se aposentar
<<<<<<<< FINISH

>>>>>>>> INSERT
55 29
======== EXPECT
Nao pode se aposentar
<<<<<<<< FINISH
```


[Código](./C/draft.c)
