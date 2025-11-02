import util

'0x6c5cec8'
'0x6c5cecc'
#part1: 0x877427a
part1 = b'\xc8\xce\xc5\x06'
part2 = b'\xcc\xce\xc5\x06'

print(f"part1: {part1}")
print(f"part2: {part2}")

payload = 4 * part1 + part2

connection = util.connectPwnable('col')
executable = util.Executable('col', connection)

program = executable.run(payload)
program.interactive()





