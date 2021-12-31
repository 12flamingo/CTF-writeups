# Diffie's Key Exchange pt. 2 (895 pts)
**Category**: Cryptography

## Challenge Description
Diffie learnt that his implementation of the system wasn't secure :<< and made some changes. Try it now!  
Connect here: `nc challs.sieberrsec.tech 1338`

## File(s)
_**chall.py**_
```python
import random
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.number import getPrime, long_to_bytes
from Crypto.Util.Padding import pad


with open('flag.txt', 'rb') as f:
    flag = f.read()


g = 5
p = getPrime(512)
a = random.randrange(2, p - 1)
A = pow(g, a, p)


print("WELCOME TO DIFFIE'S KEY EXCHANGE!!!!!\n")
print(f'g: {g}', f'p: {p}', sep='\n')

B = int(input("\nWhat is your public key?\n"))


if not 1 < B < (p - 1):
    print('Sneakyyyyy....')
    exit()
else:
    shared_secret = pow(B, a, p) 
    key = hashlib.md5(long_to_bytes(shared_secret)).digest()
    cipher = AES.new(key, AES.MODE_ECB) 
    enc = cipher.encrypt(pad(flag, 16))
    print(f'\nencrypted flag: {enc.hex()}')
```
---
## Solution
Eyeballing chall.py would tell us that we cannot directly procure the shared secret because 1. We no longer have control over the private key `a` 2. We don't know public key `A`.
So some (hopefully small amount) of brute-forcing would probably be needed.  

Unlike part 1, it appears that one requires at least some rudimentary understanding of **Diffie-Hellman (DH)** and its loopholes to work on part 2. Therefore, the Google-ing began. After a few more moments, I stumbled upon a series of discussions on stack exchange [REF] as well as an interesting report detailing "How to Backdoor Diffie-Hellman" [REF]. These helped me to realise that we would probably need to perform a **Small Subgroup Attack**. I proceeded to spend another half hour diving into the math behind the technique before recalling that the CTF was happening under timed conditions (See Post-CTF review for detailed underlying thoery)

There are three main steps to get our flag:  
### Step 1: Find subgroup of order i as small as possible, >2 
Wikipedia says,
> (Diffie-Hellman) uses the multiplicative group of integers modulo p, where p is prime, and g is a primitive root modulo p. [REF]

Since p is prime, the order of group Z_p^* that DH is using has subgroups [Lagrange's Theorem]. What we want to do is to narrow down the possible range of shared key to the much smaller subgroup. The order of this subgroup will be a factor of the order of group Z_p^* (which is p-1) [Euler's totient function] - hence we will find the smallest factor of (p-1).

### Step 2: Find generator of subgroup 


## Post-CTF review
* discrete logarithm problem

## References
