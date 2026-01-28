#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
int main(int argc, char *argv[])
{
  char buf[7] = { 0 };
	int fd = open("/dev/urandom", O_RDONLY);
  int r = read(fd, buf, 6);
  close(fd);
  return EXIT_SUCCESS;
}
