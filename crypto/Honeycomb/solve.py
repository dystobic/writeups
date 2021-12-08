#!/usr/bin/env python3

from pwn import xor

class HoneyComb:
    def __init__(self, key):
        self.vals = [i for i in key]
        
    def turn(self):
        self.vals = [self.vals[-1]] + self.vals[:-1]
        
    def encrypt(self, msg):
        keystream = []
        while len(keystream) < len(msg):
            keystream += self.vals
            self.turn()
        return bytes([msg[i] ^ keystream[i] for i in range(len(msg))]).hex()

enc = bytes.fromhex('632a0c6d68a7e5683601394c4be457190f7f7e4ca3343205323e4ca072773c177e6e')
msg = b'flag{'

for i in range(255):
    k = [enc[x] ^ (msg + bytes([i]))[x] for x in range(6)]
    hc = HoneyComb(k)
    print(bytes.fromhex(hc.encrypt(enc)))
