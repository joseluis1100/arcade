#include <stdio.h>

int main() {
    int x;
    //scanf exige "%(tipo da variável)", &(variável)
    //%d é usado para inteiros
    scanf("%d", &x);
    //no printf a cada %(tipo da variável) encontrado 
    //dentro das aspas, uma varível irá substituí-lo 
    //na ordem que é dada.
    printf("%d\n", x);
    return 0;
}