#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

pt     = bytes.fromhex('aaaaaaaaaaaaaaaa')
pt_enc = bytes.fromhex('54c9d7495d1140248892a299dc662e55')
ct_enc = bytes.fromhex('cc9ceb2fbcb61055b11923fe41124016b736af8c9d6828cb796209eee828f036325d26d5a6e5788cecda2974f4db7255abe0c85285b50df84c74dc024784da758b17c4d37d0c2f5bf3d9ed712c28605aa0fe7a33fe6058f0428ae1b54fd4a053')

alphabet = b'0123456789abcdef'
k_const = b'cyb3rXm45!@#'

lookup_table = {}

for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                k = bytes([a]) + bytes([b]) + bytes([c]) + bytes([d])
                key = k_const + k
                cipher = AES.new(key, mode=AES.MODE_ECB)
                t = cipher.encrypt(pad(pt, 16))
                lookup_table[t] = k

for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                k = bytes([a]) + bytes([b]) + bytes([c]) + bytes([d])
                key = k + k_const
                cipher = AES.new(key, mode=AES.MODE_ECB)
                t = cipher.decrypt(pt_enc)
                if t in lookup_table:
                    k1 = k_const + lookup_table[t]
                    k2 = k + k_const
                    cipher = AES.new(k2, mode=AES.MODE_ECB)
                    ct_temp = cipher.decrypt(ct_enc)
                    cipher = AES.new(k1, mode=AES.MODE_ECB)
                    ct = cipher.decrypt(ct_temp)
                    print(ct)

