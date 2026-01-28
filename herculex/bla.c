#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char *argv[])
{
    ssize_t random_bytes_read;
    int random;
    uint random_u32_seed;
    int urandom_fd;
    
    urandom_fd = open("/dev/urandom",0);
    random_bytes_read = read(urandom_fd,&random_u32_seed,4);
    if (random_bytes_read != 4) {
        puts("/dev/urandom error");
                                        /* WARNING: Subroutine does not return */
        exit(0);
    }
    close(urandom_fd);
    srand(random_u32_seed);

    random = rand();
    int a = random * -0x21524111 + (uint)(0xcafebabd < (uint)(random * -0x21524111)) * 0x35014542;
    
    printf("%d\n", a);
}
