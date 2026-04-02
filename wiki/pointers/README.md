# Introdução aos Ponteiros

## Módulo 10: Ponteiros

Uma das construções arquitetônicas mais icônicas da linguagem C. Diferentemente de uma variável fundamental que alicerça os conteúdos estáticos computacionais lógicos, um **Ponteiro** acomoda especificamente um _Endereço Numérico de Memória Física_ para alguma localização de sistema predefinida.

A sintaxe condicional de criação utiliza um `*`. O vínculo real relacional no assinalamento exige do ponteiro base buscar a notação restrita de endereço (`&`).

```c
int valor = 10;
int *ponteiro_p = &valor;

// Para reescrever logicamente algo com precisão alterando diretamente a memória que o ponteiro aponta:
*ponteiro_p = 25;
// Imediatamente o campo "valor" primitivo passa a denotar valor = 25.
```

Os ponteiros abrem portas vitais também ao funcionamento de repasse de argumentos em funções ativando efetivamente a "Passagem por Referência" com extrema formalidade.

### Operadores de Ponteiros
- `*` (dereference): Acessa o valor no endereço apontado
- `&` (address-of): Obtém o endereço de memória de uma variável
