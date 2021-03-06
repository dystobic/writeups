## Intro
**Boombastic** was a crypto challenge at FwordCTF 2021.  

Following Kerkhoff's principle you were given access to the [source](boombastic.py) of a program mimicing some kind of cinema
where you could either withdraw some ordinary tickets at random or actually enter the cinema if you provide a special VIP ticket.

Of course, we want to enter the cinema!

## Investigation
The ticket generation function in use derives a ticket `T = {r,s,p}` from a message `M` by calculating  
```
r = (y^2-1) (x^2 )^(-1)     (mod p)
s = (y+1) x^(-1)            (mod p)
```
where  
- `p` is a random prime
- `x ∈ Z_p` is a random secret 
- `y` is the numerical representation of `M` obtained by its SHA256 hash value

We are also given an encryption oracle from which we can obtain random tickets generated by the program.  

## Solution
The weakness here is that the same secret `x` is being re-used in all tickets. For we know all the other parameters involved in ticket generation, if we know `x`, we can forge any ticket - as it's the same in every ticket. Thus, given the encryption oracle we obtain a random ticket `T = {r,s,p}` and derive `x` as follows:  
```
s = (y+1) x^(-1)                (mod p)

=> x^(-1) = s/(y+1)             (mod p) // (1)
=> x = (s/(y+1)^(-1)            (mod p) // (2)

r = (y^2-1) (x^2 )^(-1)         (mod p)
  = (y^2-1) x^(-1) x^(-1)       (mod p) // substitute with (1)
  = (y^2-1) (s/(y+1))^2         (mod p)

=> y = (-s^2-r) (r-s^2)^(-1)    (mod p) // (3)

substitute (2) with (3)
```

A last quick look into the [source](boombastic.py) tells us the message `M` to be used for the VIP ticket is *Boombastic*.  

Now we have all we need to craft us some VIP ticket by ourselves and enter the cinema!

See [exploit](exploit.py) for an implementation.

> Here is your flag : FwordCTF{4ct_l1k3_a_V1P_4nd_b3c0m3_a_V1P}, enjoy the movie sir
