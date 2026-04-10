# Comandos de Repetição e Iterações

## Módulo 5: Estruturas de Repetição

A eficácia estrutural na Computação reside muitas vezes no uso inteligente de loops e laços iterativos.

### 5.1 Repetição Controlada (`for`)
Ideal para algoritmos que delimitam formalmente na compilação quantas passagens ocorrerão. O escopo conta com (1) a origem, (2) restrição condicional de continuação e (3) passo de incremento/decremento (`i++`, `--i`).
```c
for (int i = 0; i < N; i++) {
    // Processamento estrito ocorrendo N vezes
}
```

### 5.2 Avaliação Situacional (`while`)
Os laços condicionais funcionam adequadamente onde o fim da instrução ocorre submetida puramente por uma regra lógica flexível (ou sentenças condicionadas com uma *flag* especial).

```c
int entrada;
scanf("%d", &entrada);

while (entrada != 0) {
    // Escopo de processamento

    // Atualização da regra ou repetição do scanf ao fim para não causar LOOPS INFINITOS LETAIS:
    scanf("%d", &entrada);
}
```

As palavras restritas `break;` e `continue;` controlam sub-operações em repetições. O primeiro extingue imediatamente qualquer processamento residual iterativo do laço e salta para a linha adiante. O segundo cancela exclusivamente aquela rodada da iteração corrente e pula pontualmente para o início do próximo laço condicional.

### 5.3 A Geração de Números Aleatórios (`<stdlib.h>` e `<time.h>`)
Nesta etapa de aprendizado, introduziremos duas importantes bibliotecas: `<stdlib.h>` (responsável por prover utilitários gerais limitados neste ponto) e `<time.h>` (utilizada para leitura do relógio real da máquina).

Constantemente usado para simulações ou preenchimentos, a linguagem C forja algarismos estocásticos baseando-se essencialmente em uma "semente temporal" (o relógio exato do processamento).
```c
#include <stdlib.h>
#include <time.h>

int main() {
    // A alimentação temporal baseada na hora local é o suficiente para prover aleatoriedade
    srand(time(NULL)); 
    
    // rand() retorna valores absolutos longos. Utilizamos (%) para encapsular um limite. Ex (1 a 100):
    int numero_aleatorio = (rand() % 100) + 1;
    return 0;
}
```
