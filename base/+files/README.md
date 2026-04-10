# Arquivos e Persistência de Dados

## Módulo 12: Arquivos

Para evitar a desqualificação de informações colhidas em processamentos isolados efêmeros de RAM, o uso intensivo de gravadores de dados contínuos sistêmicos abrigados num arquivo sólido externo torna-se o modelo fundamental adotado por arquivos do computador. O tráfego abotoado é intermediado com predefinições relativas ao macroestrutural comando file (*FILE \**) e o operador referencial condizente `fopen`.

A manipulação abrangerá:
- `r` - Abertura base puramente dedicada ao caráter exclusivista restrito de Leitura Estrita (*Read*).
- `w` - Conduta incisiva de Criação ou Reescrutínio gravado apagando o rastreio base se porventura existir (*Write*).
- `a` - Modelagem construtiva Aditiva agregada à fenda ou rodopé referencial subjacente atual do arquivo (*Append*).

```c
FILE *arq = fopen("bancoConfigurativo.txt", "w");
if (arq != NULL) {
    fprintf(arq, "Registro formal protocolado com sufixação temporal: %d\n", 2024);
    fclose(arq); // Compulsório o selamento da etapa sistêmica com o intuito focado em limpeza de Buffers inconstantes pendentes.
}
```
Existem funções adequadas para ler bloco por bloco `fread()`, iterar por fluxos paritários `fseek()` e interagir com estruturas formativadas em matriz linear binária restrita.

### 12.1 Leitura até o Fim de Arquivo (EOF)
Listas extensas que envolvem leitura de blocos sistêmicos requerem em geral contadores que encerram abruptamente quando topam com o marcador especial subjacente em arquivos.  
Podemos empregar a função `feof(arq)` nas repetições, ou simplesmente testar o retorno do formato principal comparativamente ao `EOF`.
```c
char caractere;
// Enquanto a busca retornar elementos absolutos que não representam Final-Lógico-Físico-De-Arquivo
while ( (caractere = fgetc(arq)) != EOF ) { 
    printf("%c", caractere);
}
```
