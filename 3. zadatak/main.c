#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i;
    printf("unesite duzinu niza: ");
    scanf("%d", &n);
    int niz[n];
    printf("unesite clanove niza: ");
    for(i = 0; i < n; i++)
        scanf("%d", &niz[i]);
    for(i = 0; i < n; i++)
    {
        if(*(niz+i)%3 == 0)
            printf("%d ", *(niz+i));
        else
            continue;
    }

}
