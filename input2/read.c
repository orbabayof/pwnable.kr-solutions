#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	printf("Stage 4 clear!\n");	
  char buf[4] = "bla";
  int fd = open("\x0a", O_RDONLY); 
  int r = read(fd, buf, sizeof(buf));
  close(fd);

  return EXIT_SUCCESS;
}
