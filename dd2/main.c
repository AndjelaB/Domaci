#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char str[50], c;
    int br = 0, i;
    FILE* f = fopen ("file.txt", "w+");
    printf("Unesite string: ");
    scanf("%s", str);
    getchar();
    fprintf(f, "%s", str);
    printf("Unesite karakter: ");
    scanf("%c", &c);
    fseek(f,0,SEEK_SET);
    int n;
    n = strlen(str);
    for(i = 0; i < n; i++){
        if (c == fgetc(f)){
            br++;
        }
    }
    printf("pojavljuje se %d puta u unesenom stringu", br);
    return 0;
}
