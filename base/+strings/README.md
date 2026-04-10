# Arrays de Caracteres (Strings)

## Módulo 7: Arrays de Caracteres (Strings)

Em C, não existe um bloco funcional isolado chamado estritamente `string`. Elas são emuladas internamente valendo-se puramente de uma estrutura de tamanho previsível em *Arrays* do tipo abstrato `char`.

### Bibliotecas de Manipulação de Texto (`<string.h>` e `<ctype.h>`)
A partir deste módulo de listas, utilizaremos massivamente arranjos textuais inteiros. C traz duas bibliotecas prontas para essas formatações:
- A **`<string.h>`** abarca todos os comandos universais como `strlen()`, `strcpy()`, `strcmp()` e `strcat()`.
- A **`<ctype.h>`** opera sobre a lógica individual de letra-a-letra (como converter maiúscula em minúscula via `toupper()` e `tolower()`, ou verificar numéricos nativos com `isdigit()`).

Para que essas bibliotecas e funções padrão encontrem de forma rápida e diferenciem o limite útil textualmente de todo o lixo alocado na memória à frente de uma frase, estabeleceu-se o chamado caractere "**Terminador Nulo** (`\0`)". Desta forma: Para reservar um array de 5 letras ativas textuais (ex: "Teste"), torna-se compulsória a reserva de uma declaração base `char[6]`.

```c
#include <string.h> 

char nome[100];
    
// Ignorando buffers com problema de tecla ENTER em scanf para coletar todo o texto corrido:
scanf(" %[^\n]", nome);

// Funções provenientes da biblioteca <string.h> 
int len = strlen(nome);
char backup[100];

// Cópia profunda correta (O operador `=` de assinalamento em Strings completas é fisicamente incorreto).
strcpy(backup, nome); 

if (strcmp(backup, "TESTE") == 0) {
    // Strings Iguais!
}
```

### 7.1 Matrizes de Caracteres (Vetor de Nomes)
Para reter uma coletividade de nomes curtos ou frases na mesma estrutura unânime (um "Vetor de Strings"), demanda-se o agrupamento de matrizes bidimensionais predefinindo categoricamente a quantidade de palavras X o tamanho da fenda individual máxima delas: `char nomes[5][100];` (armazena 5 palavras contendo tolerância respectiva para 100 letras exclusivas cada uma).
