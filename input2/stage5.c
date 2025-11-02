
#include <arpa/inet.h>
#include <assert.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

static const char* socket_port = "12345";

static void stage5_socket()
{
  static const char* local_host = "127.0.0.1";
  int socket_fd = socket(AF_INET, SOCK_STREAM, 0);
  assert(socket_fd != -1);

  struct sockaddr_in server_data = 
  {
    .sin_family = AF_INET,
    .sin_port = htons( atoi(socket_port) ),
    .sin_zero = {0}
  };
  //part of init
  inet_aton(local_host, &server_data.sin_addr);

  int connect_status = connect(socket_fd, (struct sockaddr*)&server_data, sizeof(server_data));
  char sock_input[] = "\xde\xad\xbe\xef";
  int send_status = send(socket_fd, sock_input, strlen(sock_input), 0);

  close(socket_fd);   
}

int main(int argc, char *argv[])
{
  stage5_socket();
  return EXIT_SUCCESS;
}
