# Questão 29

Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a+b onde a e b são os números aleatórios.  Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quantas vezes o aluno acertou.

<details>
  <summary>Resposta</summary>

```c
#include <stdio.h>
//iremos usar para importar a função de gerar números aleatórios
#include <stdlib.h>
//para gerar algo aleatório é necessário uma semente, iremos usar a hora atual do computador
#include <time.h>

int main() {
    //implantando a semente
    srand(time(NULL));
    //a função rand gera o número aleatório de 0 ao limite do int, o módulo limita para 99, e o +1 tranforma em 1 até 100
    int a = rand() % 100 + 1;
    int b = rand() % 100 + 1;
    int resposta, acertos = 0;
    printf("qual é a soma de %d + %d? ", a, b);
    scanf("%d", &resposta);
    if(resposta == a + b) {
        printf("acertou!\n");
        acertos++;
    } else {
        printf("a resposta correta era %d\n", a + b);
    }
    a = rand() % 100 + 1;
    b = rand() % 100 + 1;
    printf("qual é a soma de %d + %d? ", a, b);
    scanf("%d", &resposta);
    if(resposta == a + b) {
        printf("acertou!\n");
        acertos++;
    } else {
        printf("a resposta correta era %d\n", a + b);
    }
    a = rand() % 100 + 1;
    b = rand() % 100 + 1;
    printf("qual é a soma de %d + %d? ", a, b);
    scanf("%d", &resposta);
    if(resposta == a + b) {
        printf("acertou!\n");
        acertos++;
    } else {
        printf("a resposta correta era %d\n", a + b);
    }
    a = rand() % 100 + 1;
    b = rand() % 100 + 1;
    printf("qual é a soma de %d + %d? ", a, b);
    scanf("%d", &resposta);
    if(resposta == a + b) {
        printf("acertou!\n");
        acertos++;
    } else {
        printf("a resposta correta era %d\n", a + b);
    }
    a = rand() % 100 + 1;
    b = rand() % 100 + 1;
    printf("qual é a soma de %d + %d? ", a, b);
    scanf("%d", &resposta);
    if(resposta == a + b) {
        printf("acertou!\n");
        acertos++;
    } else {
        printf("a resposta correta era %d\n", a + b);
    }
    printf("Acertos: %d\n", acertos);
    return 0;
}
```

</details>

## Casos de Teste

```
>>>>>>>> INSERT
10
20
30
40
50

======== EXPECT
qual é a soma de 19 + 6? a resposta correta era 25
qual é a soma de 93 + 17? a resposta correta era 110
qual é a soma de 50 + 68? a resposta correta era 118
qual é a soma de 80 + 89? a resposta correta era 169
qual é a soma de 25 + 22? a resposta correta era 47
Acertos: 0
<<<<<<<< FINISH

```


[Código](./C/draft.c)
