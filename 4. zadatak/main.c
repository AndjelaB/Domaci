#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, max;
    printf("broj elemenata niza: ");
    scanf("%d", &n);
    int niz[n];
    for(i = 0; i < n; i++)
        scanf("%d", niz+i);

    for(i = 0; i < n; i++)
    {
        if(i == 0)
            max = *(niz + i);
        if(*(niz + i) <= *(niz + i - 1))
            max = *(niz + i - 1);
    }
    printf("%d", max);
    return 0;
}
