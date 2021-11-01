___
# Tweetybirb
_(pwn, 269 points)_

Pretty standard birb protection (nc 143.198.184.186 5002)

[tweetybirb](./tweetybirb)
___

# Investigation

Running `checksec` against the binary verifies the hint in the challenge description that stack canaries are in use. An `ltrace` on the binary reveals a format string vulnerability by improper use of `printf` as well as a buffer overflow vulnerability caused by the unsafe `gets` function. Reading the symbols from the binary we find a `win` function within yielding the flag when executed.

# Solution

Leak the stack canary via the format string. Then use it before overwriting the return address of `main` with the address of `win` via the buffer overflow.

see [exploit](./exploit.py) for an automation of the exploit written in python.

> kqctf{tweet_tweet_did_you_leak_or_bruteforce_..._plz_dont_say_you_tried_bruteforce}
