#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void gets(char*);

void func(int key){
        char overflowme[32];
        printf("overflow me : ");
        gets(overflowme);       // smash me!
        if(key == 0xcafebabe){
                printf("you won!\n");
        }
        else{
                char* keyc = (char*)(&key);
                printf("val of key is [%c,%c,%c,%c]\n\n", keyc[0], keyc[1], keyc[2], keyc[3]);
        }
}
int main(int argc, char* argv[]){
        func(0xdeadbeef);
        return 0;
}

