#include <arpa/inet.h>
#include <assert.h>
#include <string.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/socket.h>

static const char* socket_port = "12345";

static char** stage1_argv(void)
{
  char** new_argv = calloc(101, sizeof(char*));
  for(int i = 0; i < 101; ++i)
  {
    new_argv[i] = "";
  }

  new_argv[0] = "./input2";
  new_argv['A'] = "\x00";
  new_argv['B'] = "\x20\x0a\x0d";
  new_argv['C'] = (char*)socket_port;
  new_argv[100] = NULL;
  return new_argv;
}

//will close the stdfd
static void pipe_to_stdfd(const char* str, int stdfd)
{
  int fd[2];
  pipe(fd);
  close(stdfd);
  dup2(fd[0], stdfd);
  write(fd[1], str, 4);
}

//closes stderr, stdin
static void stage2_stdio(void)
{
  static const char buf_stdin [] = "\x00\x0a\x00\xff";
  static const char buf_stderr[] = "\x00\x0a\x02\xff";

  pipe_to_stdfd(buf_stdin, STDIN_FILENO);
  pipe_to_stdfd(buf_stderr, STDERR_FILENO);
}

static char** stage3_env(void)
{
  char** env = calloc(2, sizeof(char*)); 
  env[0] = "\xde\xad\xbe\xef=\xca\xfe\xba\xbe";
  env[1] = NULL; 
  return env;
}

static void stage4_file(void)
{
  int fd = open("\x0a", O_CREAT | O_WRONLY);
  int written = write(fd, "\x00\x00\x00\x00", 4);
}

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

int main()
{
  //stage_1
  char** new_argv = stage1_argv();
  stage2_stdio();
  char** new_env = stage3_env();
  stage4_file();
  
  if(fork() == 0)
  {
    execve("./input2", new_argv, new_env);
    free(new_argv);
    free(new_env);
    return 0;
  }
  else 
  {
    sleep(1);
    stage5_socket();
  }
  


  return EXIT_SUCCESS;
}
