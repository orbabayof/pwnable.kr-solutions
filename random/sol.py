# wanted xor = 0xcafebabe /  3405691582
# random will always be 0x6b8b4567 / 1804289383

xor = 0xcafebabe
random = 0x6b8b4567
key = 0xa175ffd9

print(f"key is {key}")
print(f"key ^ random = {hex(key ^ random)}")

print(hex(0x6b8b4567 ^ 0xcafebabe))
print(hex(0xa175ffd9 ^ 0x6b8b4567))



# in bytes:
# wanted xor = 11001010111111101011101010111110
# random =     01101011100010110100010101100111


