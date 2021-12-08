#!/usr/bin/python3

from math import gcd

PDF_MAGIC_NUMBER = [0x25, 0x50, 0x44, 0x46, 0x2d]

def solve_a_b(enc):
    aa =  [i for i in range(256) if gcd(i, 256) == 1]
    bb = range(256)
    for a in aa:
        for b in bb:
            pdf_magic_number_enc = b''
            for n in PDF_MAGIC_NUMBER:
                pdf_magic_number_enc += bytes([(a * n + b) % 256])
            if pdf_magic_number_enc == enc[:5]:
                return a, b

if __name__ == '__main__':
    with open('encrypted.bin', 'rb') as f:
        enc = f.read()

        a, b = solve_a_b(enc)

        dec = b''
        for c in enc:
            for i in range(256):
                if (a * i + b) % 256 == c:
                    dec += bytes([i])
                    break

        o = open('letter.pdf', 'wb')
        o.write(dec)
        o.close()

