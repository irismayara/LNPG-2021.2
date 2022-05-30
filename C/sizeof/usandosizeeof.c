#include <stdio.h>

int main(){
    int a;
    float b;
    double c;
    long d;
    char e;

    printf("A variavel A eh um INTEIRO  e tem %d bytes.\n", sizeof(a));
    printf("A variavel B eh um FLOAT  e tem %d bytes.\n", sizeof(b));
    printf("A variavel C eh um DOUBLE  e tem %d bytes.\n", sizeof(c));
    printf("A variavel D eh um LONG  e tem %d bytes.\n", sizeof(d));
    printf("A variavel E eh um CHAR  e tem %d bytes.\n", sizeof(e));

    return 0;
}