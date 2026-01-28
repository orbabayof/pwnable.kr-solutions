#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[], char *env[])
{
  puts("printing env");
	putenv("PATH=/home/or/pwnable.kr-solutions/cmd1");
  printf("%s\n",getenv("PATH"));
  return EXIT_SUCCESS;
}
