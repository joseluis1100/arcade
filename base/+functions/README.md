# Construção de Funções e Recursos de Escopo

## Módulo 9: Funções e Escopo

O desmembramento funcional em sub-rotinas diminui a complexidade teórica global e possibilita reutilização de um código através da parametrização limpa. A forma da Função é delineada sempre estipulando (Tipo de Resposta) (Nome Explícito Da Tarefa) -> ((Múltiplos Parâmetros)). As funções operam baseando suas validações exclusivas perante *Variáveis Locais*.

```c
float calcularJurosRendimento(float capital, int meses) {
    float totalizado = capital + (meses * 0.15f);
    return totalizado;
} 
```

Caso precise compartilhar arrays nas transições via parâmetro, C sempre repassa vetores a partir do modelo de *Passagem por Referência*, implicando que as alterações do array dentro da construção da função irão modificar integralmente sua variante matriz original na estrutura de execução.
