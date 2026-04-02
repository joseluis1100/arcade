# O Poder da Alocação Dinâmica

## Módulo 11: Alocação Dinâmica de Memória

Problemas dimensionais frequentemente acometem os Arrays estáticos originais, já que eles proíbem expansão ao longo do fluxo contínuo. 

É neste ponto cronológico que destravamos o verdadeiro e completo poder da **`<stdlib.h>`** (a *Standard Library*). Introduzida timidamente no Módulo 3 apenas para geração de números randômicos, excluíndo suas atuações generalistas de tela, ela provê o poderoso catálogo de funções matrizes de memórias alocáveis flexíveis atreladas a ponteiros!

- **`malloc(size)`:** Aloca uma área isolada do programa na quantidade quantitativa física especulada exata repassando a ligação da matriz sob estrutura nula, exigindo na declaração original a conversão dimensional explícita (*Casting*) correspondente untrue ao peso sistêmico referencial (*sizeof*).
- **`calloc(count, size)`:** Formaliza múltiplos indexadores baseados no acúmulo individual idêntico zerado.
- **`realloc(ptr, newSize)`:** Modifica ou estende o escopo quantitativo de um processamento já consolidado alocativo.
- **`free(ptr)`:** Obrigatoriedade inegociável programática do autor para destituir ou limpar completamente uma vaga da sua arquitetura gerencial após exaurida utilidade.

```c
// Alocando e desobstruindo espaço formal em C para um ponteiro abrigar 10 Inteiros base:
int *vetorDiamico = (int *) malloc(10 * sizeof(int));
free(vetorDiamico);
```
