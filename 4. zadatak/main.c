#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, max = 0;
    printf("broj elemenata niza: ");
    scanf("%d", &n);
    int niz[n];
    for(i = 0; i < n; i++)
        scanf("%d", niz+i);

    for(i = 0; i < n; i++)
    {
        if(max <= *(niz + i))
            max = *(niz + i);
    }
    printf("%d", max);
    return 0;
}
