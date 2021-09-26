## Intro
**Substitution Cipher I** was a crypto challenge at DownUnderCTF 2021.  

You were given the encrypted flag and a .sage file.

## Investigation
The encryption scheme found in the source is a trivial substitution cipher based on the polynomial

```
13x^2 + 3x + 7
```

where `x` is substituted by each plaintext byte and the solution of the resulting mathematical expression is the corresponding
ciphertext byte interpreted as a unicode character. Therefore, decrypting a ciphertext byte `y` is as easy as solving the
quadratic equation

```
13x^2 + 3x + 7 = y
```

## Solution
I solved the quadratic equation for each ciphertext byte after `x` using the quadratic formula `(-b + sqrt(b^2 - 4ac)) / 2a`
ignoring all the negative solutions as I know the plaintext consisted of only positive byte values.  

See [exploit](./exploit.py) for an implementation written in python.

> DUCTF{sh0uld'v3_us3d_r0t_13}
