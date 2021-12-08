`2021` `CyberSecurityRumble CTF` `pwn` `bof` `strncpy` `null-termination`  

# Flag Checker, Baby
[chall.c](./chall.c)

This program is perfectly safe, right? It only tells you what you already know. Check your flags:

nc challs.rumble.host 53921
___

As `strncpy` doesn't guarantee NULL-termination, sending a non NULL-terminated string of max buffer length causes `printf` to read further characters after where the `guess`
buffer resides on the stack - where `flag` is stored.

`ruby -e 'puts "A"*31' | nc challs.rumble.host 53921`
