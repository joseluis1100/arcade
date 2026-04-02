# Variáveis e Expressões

## Módulo 1: A Estrutura Básica e as Bibliotecas Padrões

Diferentemente de linguagens interpretadas e modernas — que já incluem nativamente diversas ferramentas em sua base —, um código em linguagem C padronizada (C ANSI) precisa que suas bibliotecas de recursos sejam explicitamente declaradas.

### 1.1 A Estrutura Principal `main`
Todo programa em C precisa de uma função principal. A função `main()` é o ponto inicial de execução invocado pelo sistema operacional. O comando `return 0;` sinaliza habitualmente que a execução foi bem-sucedida.

```c
// Inclusão de biblioteca de Entrada/Saída
#include <stdio.h> 

int main() {
    // Escopo das variáveis e da lógica do programa
    return 0; 
}
```

### 1.2 Bibliotecas Iniciais e Matemáticas (`#include`)
As diretivas de pré-processamento trazem rotinas padronizadas. Neste primeiro momento de contato com a linguagem, utilizaremos puramente comandos focados em interação de console e cálculos:

| Biblioteca | Funcionalidade Principal | Exemplos a utilizar |
| :--- | :--- | :--- |
| **`<stdio.h>`** | Entrada e Saída (I/O) | `printf()`, `scanf()`, `puts()` |
| **`<math.h>`** | Funções Físicas e Matemáticas Básicas | `pow()`, `sqrt()`, `ceil()`, `floor()`, `sin()` |
| **`<stdbool.h>`** | Fornece nomes familiares ao tipo booleano | `bool`, `true`, `false` |

---

## Módulo 2: Tipos Básicos, Variáveis e Operadores

Uma variável é uma região previamente declarada na memória RAM projetada para conter um determinado tipo de dado. Elas devem ser concebidas explicitamente com um tipo compatível.

### 2.1 Tipos Primitivos

| Tipo  | Significado e Uso Comum | Especificador de Formatação |
| :---: | :--- | :---: |
| `int` | Valores numéricos inteiros (Exemplo: `-5`, `1000`). | `%d` ou `%i` |
| `float` | Números Reais (Ponto Flutuante), alcançado aproximadamente 6 a 7 casas decimais. | `%f` |
| `double`| Precisão Dupla de Ponto Flutuante, alcançando cerca de 15 casas de precisão. | `%lf` |
| `char` | Armazena exatamente 1 caractere presente na Tabela ASCII. Obrigatório o uso de aspas simples: `'A'`. | `%c` |

### 2.2 Operadores Aritméticos

A linguagem C dispõe dos operadores básicos (`+`, `-`, `*`, `/`) e também do **módulo** (`%`), que devolve especificamente o resto da divisão. Exemplo: Para verificar se `X` é par, checa-se se a expressão matemática `X % 2` é idêntica a `0`.

**Divisão Inteira (Truncamento):**
É importante observar qual o tipo de cada um dos operandos. Em C, a divisão entre dois inteiros gera sempre um resultado estritamente inteiro (a porção fracionária é descartada). Para extrair decimais, aplica-se uma coerção manual conhecida como **Casting**.

```c
int num1 = 7, num2 = 2;

float truncado = num1 / num2;           // Resultado: 3.0
float real = (float) num1 / num2;       // Operação Casting. Resultado: 3.5
```

### 2.3 Operadores Lógicos de Nível de Bit (Bitwise)

Requisitados frequentemente em sistemas embarcados e algumas listas teóricas, eles manipulam a estrutura binária da variável. É muito comum usar o C unicamente por essas rotinas:
- **`&` (AND Bi-a-Bit):** Retorna `1` apenas se ambos os bits forem `1`.
- **`|` (OR Bit-a-Bit):** Retorna `1` se ao menos um dos bits for `1`.
- **`^` (XOR Bit-a-Bit):** Retorna `1` se os bits forem exclusivamente divergentes.
- **`~` (Complemento / NOT):** Inverte todos os bits.
- **`<<` e `>>`:** Deslocamento em bits para esquerda ou direita (multiplicação ou divisão de binários inteiros por 2).

---

## Módulo 3: Comandos de Entrada e Saída

A interação do programa com a tela (saída) e com o teclado (entrada) depende do direcionamento formal dos endereços dessas variáveis.

### 3.1 Exibição na Tela (`printf`)
O `printf` formata blocos textuais.
- **Quebras de linha:** Para separar textos, você adiciona um `\n` ao comando de saída.
- **Tamanho Limite:** Limitação nas casas de um *float* (`%.2f`) exibe unicamente a fração de seu interesse, como `10.56`.
- **Preenchimento:** `printf("%02d", horas)` insere "zeros à esquerda" em números que ocupam apenas uma casa.

### 3.2 Aquisição via Teclado (`scanf`)
O `scanf` é o leitor fundamental de sintaxes de console. Quando informamos ao sistema onde alojar o dado digitado, utilizamos o ampersand comercial **`&`** para designar o **Endereço de Memória** daquela variável. Sem o `&`, o sistema assume de maneira errônea o "valor" como destino final.

```c
int idade;          
float salario;      

// A leitura suporta espaços contíguos na separação e formatação da máscara.
scanf("%d %f", &idade, &salario);
```
