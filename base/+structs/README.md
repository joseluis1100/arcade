# Estruturas Declaradas pelo Programador (Structs)

## Módulo 8: Estruturas Heterogêneas (Structs)

As "Estruturas Heterogêneas" englobam de forma semântica um corpo completo coeso que unifica sob uma denominação abrangente primitivos com múltiplos formatos (`char`, `int`, etc).

```c
typedef struct {
    char nome[50];
    int idade;
    float notas[3];
} Aluno;

int main() {
    Aluno registroBase;
    
    // O Acesso isolado aos componentes nativos ocorre via uso do operador '.'
    registroBase.idade = 20;
    return 0;
}
```
