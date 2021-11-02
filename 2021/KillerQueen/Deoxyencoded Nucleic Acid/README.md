___
# Deoxyencoded Nucleic Acid

[dna1.txt](./dna1.txt)
___

# Investigation

The challenge description was emphasizing that the _four_ nucleobases form an encoding. I recognized that the length of the dna sequence is 0 mod 4 and took an educated guess that a sequence of _four_ nucleobases encodes a character. As a character has 1 Byte I predicted `A`, `G`, `C` and `T` each could represent two bits. I know the flag starts with the letter `k` whose ordinal value is binary `01 10 10 11` and the dna sequence starts with `TGGC` - which matches

- `T` with `01`
- `G` with `10`
- `C` with `11`

just perfectly, leaving `A` to represent `00`.

# Solution

Interpreting each quadrupel of nucleobases as the ordinal value of a character by concatenation of their binary values yields the flag.

See [solve](./solve.py) for an implementation in python.

> kqctf{its_basica11y_base_four}
