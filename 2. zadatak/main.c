#include <stdio.h>
#include <stdlib.h>

void unosMatrice(int n, int m, int* niz)
{
    int i, j;
    printf("unesite clanove matrice: ");
    for(i = 0; i < n; i++)
        for(j = 0; j < m; j++)
            scanf("%d", niz+i*m+j);
}

void ispisMatrice(int n, int m, int* niz3)
{
    int i, j;
    for(i=0; i<n; i++)
    {
        for(j=0; j<m; j++)
        {
            printf("%d", *(niz3+i*m+j));
        }
        printf("\n");
    }
}

void zbirMatrice(int* niz, int* niz2, int* niz3, int n, int m)
{
    int i, j;
    for(i=0; i <n; i++)
    {
        for(j=0; j < n; j++)
        {
            *(niz3+i*m+j)=*(niz+i*m+j)+*(niz2+i*m+j);
        }
    }
}

int main()
{

    int n, m;
    scanf("%d%d", &n, &m);
    int niz[n][m], niz2[n][m],niz3[n][m];
    unosMatrice(n, m, niz);
    unosMatrice(n, m, niz2);
    zbirMatrice(niz, niz2, niz3, n, m);
    ispisMatrice(n, m, niz3);
    return 0;
}
