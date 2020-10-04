#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ponavljanje(char slovo, char* str)
{
    int i, br = 0;
    for(i = 0; i<strlen(str); i++)
    {
        if(slovo == str[i])
            br++;
    }
    return br;
}

int main()
{
    char slovo;
    char str[100];
    printf("rec: ");
    fflush(stdin);
    gets(str);
    printf("slovo: ");
    scanf("%c", &slovo);
    //slovo = getc(stdin);
    printf("%d", ponavljanje(slovo, str));
    return 0;
}
