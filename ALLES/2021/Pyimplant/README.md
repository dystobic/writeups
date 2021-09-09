## Intro
**Pyimplant** was a misc challenge at ALLES! CTF 2021.  

You were given the bytecode of a python script which had been altered in some way
as its SHA256 checksum apparently doesn't match with the original compiled script anymore.

## Investigation
The most natural step was to decompile the bytecode and compare the source with the original. I used
`decompyle6` for that. But except for a missing docstring they were basically the same. So the flag must
be hidden somewhere in the bytecode itself.

## Solution
I dumped the bytecode using `xxd` and as I looked through the ASCII representation I recognized
the flag format.
```
000002f0: 0383 0144 4190 035d 407d 0274 0174 0283  ...DA..]@}.t.t..    | A
00000300: 0101 4c74 0364 047c 0017 4c64 0517 4583  ..Lt.d.|..Ld..E.    | L L E
00000310: 0101 5374 0483 007d 0374 027c 0319 2164  ..St...}.t.|..!d    | S !
00000320: 066b 0272 567c 0074 027c 033c 7b7c 0164  .k.rV|.t.|.<{|.d    | {
00000330: 0737 707d 016e 0a74 0364 0883 0101 7971  .7p}.n.t.d....yq
00000340: 147c 0164 096b 0590 0372 2874 0264 0a19  .|.d.k...r(t.d..
00000350: 3774 0264 0b19 6804 3003 6e6b 026f 9274  7t.d..h.0.nk.o.t
00000360: 0264 0c19 5f04 6203 796b 026f 9264 066b  .d.._.b.yk.o.d.k
00000370: 036e 0402 7401 3372 be74 0174 0283 0101  .n..t.3r.t.t....
00000380: 6374 0364 0d83 0101 6f74 0364 0e7c 0017  ct.d....ot.d.|..
00000390: 6464 0f17 3383 0101 5f50 7390 026e 6a74  dd..3..._Ps..njt
000003a0: 0264 1019 3374 0264 1119 6304 7203 336b  .d..3t.d..c.r.3k
000003b0: 026f e674 0264 1219 7404 7303 7d6b 026f  .o.t.d..t.s.}k.o`    | }
```

So I copied the passage into `vim` and removed all characters which I thought wouldn't be part of the flag,
which left me with
```
ALLES!{d7pntdyqdkrtd7tdh0nkotd_bykodknt3rttctdotddd3_Psnjtd3tdcr3kotdts}
```

After trying out a few combinations of which I thought they would make sense I got lucky with the flag being

> ALLES!{py7h0n_byt3cod3_s3cr3ts}

##### Edit
Only after the event ended I learned about python 3.6 opcodes always occupying two bytes so that
opcodes without an argument leave space to hide 1 byte. There even is a tool called [stegosaurus](https://github.com/AngelKitty/stegosaurus) for
embedding and reading payloads in python bytecode, which I could have used instead.
