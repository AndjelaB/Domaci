#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE* f= fopen("PRIMER.txt","r");
    printf("unesite znak: ");
    char c = getc(stdin);
    fseek(f,0,SEEK_SET);
    char provera = "a";
    int counter = 0;
    while(provera!= EOF)
    {
        provera = fgetc(f);
        if(provera == c)
            counter ++;
    }
    printf("%d",counter);
    return 0;
}


