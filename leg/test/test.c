#include <stdio.h>
#include <stdlib.h>

int key()
{
	asm("mov r3, pc\n");
}
int main()
{
  printf("%d\n", key());
  return EXIT_SUCCESS;
}
