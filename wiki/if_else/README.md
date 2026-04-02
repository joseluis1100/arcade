# Comandos Condicionais e Controle de Fluxo

## Módulo 4: Comandos Condicionais e Controle de Fluxo

Os operadores condicionais promovem as lógicas baseadas em sentenças booleanas (`0` sendo Falso, e algo diverso de `0` sendo assumido como Verdadeiro).

### 4.1 Operadores de Comparação e Operadores Lógicos
Na comparação, cuidado com a estrutura do comando:  `=` atribui e altera o valor de variáveis, já o `==` verifica puramente se existe igualdade matemática. Os operadores lógicos formam sentenças complexas:
- **`&&` (AND):** Retorna verdadeiro quando toda a sentença for verdadeira simultaneamente.
- **`||` (OR):** Basta uma parte relacional ser correta para avançar positivamente no escopo de checagem.
- **`!` (NOT):** Reverte a proposição relacional de verdadeiro para falso, e vice-versa.

### 4.2 O Comando `if - else if - else`
A verificação sistemática na análise de dados avança linha-a-linha.
```c
if (nota >= 7.0) {
    printf("Aprovado.\n");
} 
else if (nota >= 5.0) {
    printf("Recuperação pendente.\n");
} 
else {
    printf("Reprovado integralmente.\n");
}
```

### 4.3 O Comando `switch - case`
Extremamente valioso para analisar menu de opções estritas, onde as variáveis assumem condições fechadas em casos lógicos inteiros ou de tipo `char`. 
Lembre-se SEMPRE de utilizar a cláusula `break;` ao término do processamento de um `case`, garantindo que casos sucessivos mais abaixo não transbordem por *fall-through*.

### 4.4 Operador Ternário (`? :`)
Uma forma concisa, recomendada estritamente para sintaxes reduzidas, combinando em suma `(Condição) ? Verdadeiro : Falso;`
