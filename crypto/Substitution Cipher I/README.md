`2021` `DownUnder CTF` `crypto` `substitution`

# Substitution Cipher I
[substitution-cipher-i.sage](substitution-cipher-i.sage) | [output.txt](output.txt)  

Just a simple substitution cipher to get started...
___

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

I solved the quadratic equation for each ciphertext byte after `x` using the quadratic formula `(-b + sqrt(b^2 - 4ac)) / 2a`
ignoring all the negative solutions as I know the plaintext consisted of only positive byte values.  

See [exploit](./exploit.py) for an implementation written in python.

> DUCTF{sh0uld'v3_us3d_r0t_13}
