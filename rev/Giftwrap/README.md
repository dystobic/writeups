`2021` `HTB Cyber Santa is Coming to Town` `rev` `upx` `xor`  

# Gift Wrapping
[giftwrap](./giftwrap)

The elves won't let you into their secret hideout without the password.
Luckily, they've given it to you as a gift! But it seems to be wrapped up tight...
___

1. Execute `strings` on binary to detect it is packed.
2. Unpack binary with `upx -d giftwrap`
3. Reverse `main`

	```C
	char input[256];
	scanf("%256s", &input);

	for (int i = 0; i < 256; i++) {
		input[i] ^= 0xf3
	}

	char check = [
	    0xbb, 0xa7, 0xb1, 0x88, 0x86, 0x83, 0x8b, 0xac,
	    0xc7, 0xc2, 0x9d, 0x87, 0xac, 0xc6, 0xc3, 0xac,
	    0x9b, 0xc7, 0x81, 0x97, 0xd2, 0xd2, 0x8e, 0x00
	];

	assert(check == input)
	```
4. [solve](./solve.py)
