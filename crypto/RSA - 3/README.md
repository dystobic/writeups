___
# RSA - 3
_(crypto, 250 points, 85 solves)_

Alright, this is the big leagues. You have someone's Public Key. This isn't unusual, if you want to send someone an encrypted message, you have to have thier public key.
Your job is to evaluate this public key, and obtain the value of the secret exponent or decryption exponent (The value of "d" in an RSA encryption).

Wrap the number that you find with dsc{<number>}!

[mykey.pub](./mykey.pub)
___

## Investigation
From the challenge description it can be deduced that `mykey.pub` is a [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) public key.
So I first extracted the modulus `n` and public exponent `e` from it with `openssl rsa -in mykey.pub -noout -text -pubin`. Looking at a _very_ big `e`
I took an educated guess that maybe `d` would be sufficently small (namely `d < 1/3n^(1/4)`), which could then be exploited by leveraging
[Wiener's Attack](https://en.wikipedia.org/wiki/Wiener%27s_attack).

## Solution
Using Wiener's Attack based on continued fractions and their convergents I was able to recover `d` from the public key.

See [exploit](./exploit.py) for an implementation in python.

> dsc{6393313697836242618414301946448995659516429576261871356767102021920538052481829568588047189447471873340140537810769433878383029164089236876209147584435733}
