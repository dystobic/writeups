___
# Break me!
_(crypto, easy, 100 points, 163 solves)_

AES encryption challenge.

Author: 2keebs

`nc pwn-2021.duc.tf 31914`

[aes-ecb.py](./aes-ecb.py)
___

## Investigation
We are faced with an [AES-ECB](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB)) encryption oracle here which - given some plaintext _**P**_ - encrypts

```
flag + P + k + padding
```

where _**k**_ is the secret key used in the encryption scheme.

## Solution
Because we control _**P**_, we can leak the key bytes one-after-another by leveraging a [well-known](https://crypto.stackexchange.com/a/46921) chosen plaintext/brute-force attack. As soon as the key is reconstructed it can then be used to
decrypt the first blocks independently resulting in our flag. For this particular challenge, key memoization and a reconnection mechanism had to be implemented as the remote host did from time to time just close the connection.

See [exploit](./exploit.py) for an implementation of the attack written in python.

> DUCTF{ECB_M0DE_K3YP4D_D474_L34k}}
