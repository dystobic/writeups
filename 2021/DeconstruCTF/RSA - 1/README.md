___
# RSA - 1
_(crypto, 150 points, 191 solves)_

I have a lot of big numbers. Here, have a few!

[big_numbers.txt](./big_numbers.txt)
___

## Investigation
Obviously, this is a RSA challenge and despite they are calling them big_numbers, those numbers aren't _that_ big. Therefore, `n` can be factored out with reasonable efforts.

## Solution
Someone already did the factorization of `n` and so I was able to fetch the corresponding `p` and `q` from [factordb](http://factordb.com/). From that point I just
followed basic schoolbook RSA algorithm to derive `d` and decrypt `c`.

See [exploit](./exploit.py) for an implementation in python.

> dsc{t00_much_m4th_8898}

