#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
	srand(time(NULL));
	int r1 = rand();
	srand(r1);
	int r2 = rand();
	printf("%d\n", (int)(r1/r2) % 1000);

	return 0;
}
