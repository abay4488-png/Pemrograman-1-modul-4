#include <stdio.h>

int main() {
    int a, b;
    if (scanf("%d %d", &a, &b) == 2) {
        if (a < b) {
            for (int i = a, j = b; i <= b; i++, j--) 
            printf("%d %d%s", i, j, (i < b) ? " - " : "");
        } else {
            for (int i = a, j = b; i >= b; i--, j++) 
            printf("%d %d%s", i, j, (i > b) ? " - " : "");
        }
        printf("\n");
    }
    return 0;
}