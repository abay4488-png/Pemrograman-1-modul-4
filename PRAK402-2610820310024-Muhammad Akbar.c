#include <stdio.h>

int main() {
    int n;

    if (scanf("%d", &n) == 1) {
        
        for (int i = 1; i <= n; i += 2) {
            printf("%d", i);
            if (i + 2 <= n) {
                printf(" ");
            }
        }
        printf("\n");

        int mulai_genap = (n % 2 == 0) ? n : n - 1;

        for (int i = mulai_genap; i >= 2; i -= 2) {
            printf("%d", i);
            if (i - 2 >= 2) {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}