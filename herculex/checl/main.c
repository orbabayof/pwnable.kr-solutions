#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

extern char *gets (char *__s);
int ropme(void)

{
    int buffer_int;
    ssize_t sVar1;
    char buffer [100];
    int exp_guess;
    int local_10;
    
      printf("How many EXP did you earned? : ");
      gets(buffer);
      buffer_int = atoi(buffer);

      puts("got here once");
      puts("You\'d better get more experience to kill Voldemort");
    return 0;
}

int main(int argc, char *argv[])
{
  ropme();
  return EXIT_SUCCESS;
}
