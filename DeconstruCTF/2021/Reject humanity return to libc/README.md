___
# Reject humanity return to libc
_(binary, 250 points, 32 solves)_

Hello Agent,
<REDACTED>, a bio-terrorist organisation located in the west have stolen serum Id:<Redacted> from our special research facility.
The serum has the ability to reverse evolution of a species by 100's of years and can return humans back to their former monkey selves.
We have learnt that the organisation prepares to release the serum as a gas form in unknown public area using a dipenser.The only information we have about the dispenser is the login portal info,the login program running, and its libc version

Your mission is to break in and disarm the dispenser.The connection info,login program, and the libc library is given below.Be warned the organisation are known pranksters.

nc overly.uniquename.xyz 2052 

[challenge](./challenge) | [libc-2.31.so](./lib/x86_64-linux-gnu/libc-2.31.so) | [dispenser_login.c](./dispenser_login.c)
___

## Investigation
 _TODO writeup_

## Solution
See [exploit](./exploit.py) for an automation of the exploit written in python.

> dsc{r37URN_70_M0nk3}
