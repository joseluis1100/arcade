# Arrays (Vetores e Matrizes)

## Módulo 6: Arrays (Vetores e Matrizes)

Também chamadas de estruturas homogêneas — comportam apenas um mesmo tipo primitivo e garantem o avanço através da manipulação dos seus índices matemáticos, começando habitualmente com o zero.

### 6.1 Os Limites e a Falha de Segmentação
A memória em C exige atenção máxima: Um identificador como `int numeros[10];` armazena 10 células inteiras organizadas estruturalmente do array num índice basal **0** ao teto limite condicional exclusivo de **9**. A leitura acidental com `numeros[10] = 5;` fará com que o software sobreponha fisicamente falhas conhecidas de Sistema e memória ("Segmentation Fault").

```c
// Utilização matricial bidimensional
int mat[3][3];

for (int linha = 0; linha < 3; linha++) {
    for (int col = 0; col < 3; col++) {
        mat[linha][col] = 0;
    }
}
```
