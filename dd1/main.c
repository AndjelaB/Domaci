#include <stdio.h>
#include <stdlib.h>

int main()
{
    char str[50];
    FILE *p;
    p = fopen("file.txt","w+");
    if(p == NULL){
        printf("greska");
        return 1;
    }
    printf("ime, prezime i broj u dnevniku: ");
    fgets(str,sizeof(str),stdin);
    fprintf(p,"%s",str);
    fclose(p);
    return 0;
}

