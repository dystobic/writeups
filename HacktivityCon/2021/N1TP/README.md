## Intro
**N1TP** was a crypto challenge at H@cktivityCon 2021 CTF.  

You were given an encrypted flag and an encryption oracle.

## Investigation
From the context of the challenge one can deduce the applied encryption scheme here is a [One-Time Pad](https://en.wikipedia.org/wiki/One-time_pad). A OTP is cryptographically secure unless being re-used. If so, given an encryption oracle and a ciphertext `C = M ^ K` where `K` is the OTP , one can recover the original message `M` by simply calculating `C1 = M1 ^ K` and then:  

```
C ^ C1 ^ M1 = M ^ K ^ M1 ^ K ^ M1 = M
```

## Solution
We fetched the encrypted flag and the ciphertext for a plaintext we provided and predicted that the OTP would be re-used. Applying the aforementioned formula proved us right and rewarded us with the flag.

> flag{9276cdb76a3dd6b1f523209cd9cd9c0a11b}
