`2021` `DeconstruCT.F` `crypto` `rsa` `small exponent attack`  

# RSA - 2
[supercomputer_food](./supercomputer_food)  

Hey I heard you have a supercomputer at home. This is taking too long to compute on my computer. Could you take a look on yours?
I'm sure its a lot more precise than mine is, and faster too!
___

The numbers are obviously from the [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) encryption scheme. What immediately catches the eye here is the
very small value for `e`. Also, `c` is relatively small compared to `n`. So there's a chance that `m^e = c < n` and if no padding is used then the original message
can be recovered by just reversing the operation with `m = c^(1/e)`.

See [exploit](./exploit.py) for an implementation in python.

> dsc{t0-m355-w1th-m4th-t4k35-4-l0t-0f-sp1n3}
