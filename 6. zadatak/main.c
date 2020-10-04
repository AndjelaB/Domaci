#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define max 20

/*int jednaki(char* s1, char* s2)
{
    if(strcmp(s1, s2) == 0)
        return 1;
    else
        return 0;

}*/

int jednaki(char* s1, char* s2)
{
    int i;
    if(strlen(s1) != strlen(s2))
         return 0;
    for(i = 0; i < strlen(s1); i++)
    {
        if(s1[i] != s2[i])
            return 0;
    }
    return 1;


}

int main()
{
    char s1[max], s2[max];
    printf("prvi string: ");
    fflush(stdin);
    gets(s1);
    printf("drugi string: ");
    fflush(stdin);
    gets(s2);
    if(jednaki(s1, s2) == 1)
        printf("jednaki su");
    else
        printf("nisu jednaki");
    return 0;
}
