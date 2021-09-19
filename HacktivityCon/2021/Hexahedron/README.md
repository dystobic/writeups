## Intro
**Hexahedron** was a crypto challenge at H@cktivityCon 2021 CTF.  

You were given a file containing three hexadecimal numbers `n`, `e` and `c`.

## Investigation
The numbers look much like the modulus, public key and a ciphertext from the [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) encryption scheme.
What immediately catches the eye here is the very small value for `e`. Also, `c` is relatively small compared to `n`. So there's a chance that `m^e = c < n` and if no padding is used then the original message can be recovered by just reversing the operation with `m = c^(1/e)`.

## Solution
See [exploit](./exploit.py) for a python implementation calculating `m = c^(1/e)` and parsing the flag from the result.

> flag{080eaeb0d8f724bcb542562b3bb708e5}
