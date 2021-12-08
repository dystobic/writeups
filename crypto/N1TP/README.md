`2021` `H@cktivityCon CTF` `crypto` `one-time pad`
# N1TP

Nina found some new encryption scheme that she apparently thinks is really cool. She's annoying but she found a flag or something, can you deal with her?
___

You were given an encrypted flag and an encryption oracle. From the context of the challenge one can deduce the applied encryption scheme here is a [One-Time Pad](https://en.wikipedia.org/wiki/One-time_pad). A OTP is cryptographically secure unless being re-used. If so, given an encryption oracle and a ciphertext `C = M ^ K` where `K` is the OTP , one can recover the original message `M` by simply calculating `C1 = M1 ^ K` and then:  

```
C ^ C1 ^ M1 = M ^ K ^ M1 ^ K ^ M1 = M
```

I fetched the encrypted flag and the ciphertext for the plaintext I provided and predicted that the OTP would be re-used. Applying the aforementioned formula proved me right and rewarded me with the flag.

> flag{9276cdb76a3dd6b1f523209cd9cd9c0a11b}

##### Edit
I learned after the event that because we know the original message starts with the word `flag{` I could have chosen a plaintext for the oracle starting with the same word to learn that the OTP is being re-used here - the first bytes of the two ciphertexts are then equal and therefore the OTP is re-used.
