___
# Reject humanity return to libc
_(binary, 250 points, 32 solves)_

Hello Agent,  
`<REDACTED>`, a bio-terrorist organisation located in the west have stolen serum Id:`<Redacted>` from our special research facility.
The serum has the ability to reverse evolution of a species by 100's of years and can return humans back to their former monkey selves.
We have learnt that the organisation prepares to release the serum as a gas form in unknown public area using a dipenser.The only information we have about the dispenser is the login portal info,the login program running, and its libc version

Your mission is to break in and disarm the dispenser. The connection info,login program, and the libc library is given below. Be warned the organisation are known pranksters.

nc overly.uniquename.xyz 2052 

[challenge](./challenge) | [libc-2.31.so](./lib/x86_64-linux-gnu/libc-2.31.so) | [dispenser_login.c](./dispenser_login.c)
___

## Investigation
Looking at the provided [source](./dispenser_login.c) of the program we can spot a
common buffer overflow vulnerability in the `disarm_dispenser` function caused by
the insecure `gets` function.
The program is pretty minimal and does not contain any other function to use within our exploit - so we are going to leverage
a classical [return-to-libc attack](https://en.wikipedia.org/wiki/Return-to-libc_attack).

The exploit works in two stages:
1. Pretending that ASLR is enabled on the target system, we first leak the absolute address
of `puts@libc` in order to derive the base address of `libc` from it at runtime.
2. Using the base address of `libc` we calculate the absolute addresses of `system`
and `/bin/sh` in `libc` to spawn a shell.

As PIE is disabled on the binary and the [libc](./lib/x86_64-linux-gnu/libc-2.31.so) in use on the target system is provided, all the addresses,
offsets, strings and ROP gadgets needed for the exploit can be easily obtained in advance (e.g. using `objdump`, `strings` and `ROPGadget`).

## Solution
See [exploit](./exploit.py) for an automation of the exploit written in python.

After having access to the target system, there's a `disarm_dispencer.sh` script in the current working directory. Execute it and it prints out the flag.

> dsc{r37URN_70_M0nk3}

###### Disclaimer
Not using some of `pwntools` functionality in the exploit like ELF loading & dynamically finding addresses and offsets or building ROP chains
was intentional. I explicitely wanted to do some manual work and preparation of the attack in order
to consolidate my knowledge.
