from pwn import *

#the script has a change is giving N=1 C=0, little chance for that so not handles
#if doesn't work just rerun the script
def get_coins_data(p : remote):
    coin_str : bytes = p.recvline()
    print("this is what I got")
    if(str(coin_str).__contains__('Correct!')):
        coin_str = p.recvline()
    print(coin_str)
    N = int( coin_str[2:5] )
    C = int( coin_str[ str(coin_str).find('C'): str(coin_str).find('\n') ] )
    return N,C

def _generate_number_seq(start : int, finish : int) -> str:
    ret_seq = ""
    for i in range(start,finish + 1) :
        ret_seq += str(i) + ' '
    return ret_seq

def is_on_lower(low : int, high : int,p : remote):
    lower_half = _generate_number_seq(low, (low + high)//2)
    print(lower_half)
    p.sendline(lower_half.encode())
    weight = int( p.recvline() )
    print(weight)

    #if it is not even, weight includes the number 9 
    #and that means that we are looking for the lower half
    return weight % 2 != 0

def start_session(p : remote):
    p.recvuntil('- Ready? starting in 3 sec... -'.encode())
    print(p.recvline())
    print(p.recvline())
    sleep(2)

def get_fake_index(p : remote):
    low : int = 0 
    high,C = get_coins_data(p)

    while high != low:
        avg : int = (low + high)//2
        if is_on_lower(low, high, p):
            high = avg
        else:
            low = avg + 1
        C = C - 1

    for i in range(0, C):
        print('0')
        p.sendline('0'.encode())


    print(high)
#    p.interactive()
    p.sendline(str(high).encode())



p = remote('pwnable.kr',9007)
start_session(p)
for i in range(0, 100):
    get_fake_index(p)
    print(p.recvline())

p.interactive()


