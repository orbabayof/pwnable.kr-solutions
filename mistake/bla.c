
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define XORKEY 1 

void xor(char* s, int len){
	int i;
	for(i=0; i<len; i++){
		s[i] ^= XORKEY;
	}
}

int main(int argc, char *argv[])
{
  char buf[] = "A";
  xor(buf, strlen(buf));
  printf("xor A\n as number: %d\n as char %c", buf[0], buf[0]);
  return EXIT_SUCCESS;
}
