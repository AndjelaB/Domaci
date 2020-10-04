#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, j, n;
    printf("dimenzija matrice: ");
    scanf("%d", &n);
    double niz[n][n], zamena;
    printf("elementi matrice: ");

    for(i = 0; i<n; i++)
        for(j=0; j<n; j++)
                scanf("%lf", &niz[i][j]);

    for(i = 0; i<n; i++)
    {
        for(j=0; j<n; j++)
            {
                zamena = niz[i][j];
                niz[i][j]=niz[j][i];
                niz[j][i]=zamena;
                //printf("\n\n");
                //printf("niz[i][j] = %.2lf, niz[j][i] =  %.2lf", niz[i][j], niz[j][i]);
            }
    }

    for(i = 0; i<n; i++)
    {
        for(j=0; j<n; j++)
            {
                printf("%.2lf ", niz[j][i]);
            }
            printf("\n");
    }
    return 0;
}
