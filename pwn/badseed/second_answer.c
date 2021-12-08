#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
	srand(time(NULL));
	rand();
	printf("%d\n", rand());

	return 0;
}
