# Recursividade

## Módulo 8: Recursividade

A **Recursão** ocorre quando um fragmento de chamadas reexecuta perfeitamente dentro de sua avaliação algorítmica iterativa com base regressiva limitando seu final condicionado a um Caso de Base (ex. Funções Fatoriais e de Fibonacci).

Uma função recursiva é aquela que chama a si mesma para resolver um problema menor do mesmo tipo, até atingir um caso base que não requer mais chamadas recursivas.

### Exemplo: Fatorial
```c
int fatorial(int n) {
    if (n == 0 || n == 1) {
        return 1;  // Caso base
    }
    return n * fatorial(n - 1);  // Chamada recursiva
}
```

### Elementos essenciais:
1. **Caso base**: Condição de parada que retorna um valor已知
2. **Caso recursivo**: Reduce o problema a uma versão menor de si mesmo
