`2021` `HTB Cyber Santa is Coming to Town` `crypto` `rsa` `small exponent attack`

# Missing Reindeer
[message.eml](./message.eml)

Not only elves took control of Santa's Christmas factory but they kidnapped Rudolf as well.
Our cyber spies managed to capture an email related to Santa's favorite reindeer. Can you
help them decrypt the message?
__

1. Extract [public key](./key.pub) and [secret message](./secret.enc) from [email](./message.eml).
2. Parse public key with `openssl rsa -in key.pub -noout -text -pubin`
3. Parse secret with `cat secret.enc | base64 -d | xxd -p | tr -d '\n'`
4. [solve](./solve.py)
