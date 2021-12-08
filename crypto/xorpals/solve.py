from pwn import xor

with open('flags.txt') as f:
    for line in f.readlines():
        for byte in range(256):
            dec = xor(byte, bytes.fromhex(line))
            if b'dam' in dec:
                print(dec)
