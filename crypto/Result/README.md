`2021` `CyberSecurityRumble CTF` `crypto` `hash` `md5` `brute-force`  

# Result
[Test_Result.eml](./Test_Result.eml)

I really want to know my test result, but unfortunately its additionally protected. I attached the email. Maybe you can help?
___

The PDF attached in the email is password protected with a german postal code.

1. Generate a wordlist with possible german postal codes with `crunch 5 5 0123456789 > wordlist`
2. Extract the password hash from the PDF with `pdf2hashcat result.pdf > hash`
3. Crack the hash with `hashcat -m 10700 -a 0 wordlist hash` yielding `73760`
