#!/usr/bin/python3

dna = {'A': '00', 'T': '01', 'G': '10', 'C': '11'}

with open('dna1.txt') as f:
    s = f.read()

    flag = ''.join([chr(int(dna[s[i]]+dna[s[i+1]]+dna[s[i+2]]+dna[s[i+3]], 2)) for i in range(0, len(s) - 4, 4)])

    print(flag)
