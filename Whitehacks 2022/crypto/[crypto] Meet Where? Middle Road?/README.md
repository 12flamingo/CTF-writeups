# [crypto] Meet where? Middle Road? (988 pt/7 solves)
Author: WickedEye (Ying Keat)<br>
Difficulty: Medium-Hard

## Challenge description
My lecturer told me that DES is not secure and I should use AES for encryption.<br><br>Here's what I have as part of my school project to securely encrypt messages on where to meet my friends. I am sure no one can crack AES encryption.<br><br>
Challenge Access: `nc challenges2.whitehacks.xyz 41337`

### Files: 
* secure_aes.py

---
## Solution
### Recon
We are told that this involves AES encryption, and the title very kindly tells us the attack to use: "**Meet in the middle attack (AES)**" Here’s what wikipedia [1] tells us:
> When trying to improve the security of a block cipher, a tempting idea is to encrypt the data several times using multiple keys. One might think this doubles … the security … because an exhaustive search on all possible combination of keys (simple brute-force) would take 2n·k attempts if the data is encrypted with k-bit keys n times. The MITM is a generic attack that counters the benefits by _storing intermediate values from the encryptions or decryptions_ and using those to _improve the time_ required to brute force the decryption keys. The MITM attack attempts to find the keys by using both the range (ciphertext) and domain (plaintext) …

Looking back at the python code we are given, here’s what it’s doing each time you run it:
1. get_new_key() generates two random different keys with the format wH1t3H@cK5_XXXXX where X is a digit from 1 through 9 
2. encrypt() does the double AES encryption with the 2 keys before base64 encoding it
3. solve_me() is what we get to interact with:
```
Welcome to my personal encryption project
Where to meet next: <encrypted flag>

Test out this secure encryption scheme: <input from us>

<encrypted input>
```

### Solving
After connecting to the service, here’s what I had:
```
Welcome to my personal encryption project
Where to meet next: 2NlSyx27qNLT35ih/N7lqLrp9A8Z0tEhv34SGrfdORXX4RV4hAHKbpIiJVteM8qQ

Test out this secure encryption scheme: aaaaaaaaaaaaaaaa

l3sGI8MveiL31mhmINTJtIPYKZkgFIGNGWFOGyr6NCg=
```
We can break the **MITM** down into **three main steps**, as outlined in the comments:

_**solve.py**_
``` python
from random import randint
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

printable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fav_event = "wH1t3H@cK5_"
pt = 'aaaaaaaaaaaaaaaa' #my input
ct = b64decode("l3sGI8MveiL31mhmINTJtIPYKZkgFIGNGWFOGyr6NCg=".encode("utf-8")) #my input, encrypted

##STEP ONE: List all possible keys
def possible_keys():
    poss_keys = []
    for a in printable:
        for b in printable:
            for c in printable:
                for d in printable:
                    for e in printable:
                        key = fav_event + str(a) + str(b) + str(c) + str(d) + str(e)
                        poss_keys.append(key)

    return poss_keys

##STEP TWO: Using all the possible keys, encode plaintext and store in map ciphertext -> key1
def enc_pt(possible_keys):
    result = {}
    for key in possible_keys:
        key1 = key
        cipher1 = AES.new(key1.encode("utf-8"), mode=AES.MODE_ECB)
        c1 = cipher1.encrypt(pad(pt.encode("utf-8"), AES.block_size))
        result[c1] = key1
        
    return result

##STEP THREE: Similarly, decode ciphertext and look up in the map from enc_pt
def denc_ct(possible_keys, enc_pt):
    for key in possible_keys:
        key2 = key           
        cipher2 = AES.new(key2.encode("utf-8"), mode=AES.MODE_ECB)
        result = cipher2.decrypt(ct)
        if result in enc_pt: #if we find a pair that matches
            key1 = enc_pt[result] 
            return key1, key2 #we win! here is our key


def main():
    keys = possible_keys()
    enc_plaintext = enc_pt(keys)
    denc_ciphertext = denc_ct(keys, enc_plaintext)
    print(denc_ciphertext)

if __name__ == "__main__":
    main()
```

Hooray! We now have the two keys after running the above script. 
```('wH1t3H@cK5_12252', 'wH1t3H@cK5_93658')```

Now, there’s one small thing left to do. We simply reverse the order that the original flag was encoded. Essentially, **base64decode -> decrypt with key2 -> decrypt with key1** <br>

``` python
flag_en = "2NlSyx27qNLT35ih/N7lqLrp9A8Z0tEhv34SGrfdORXX4RV4hAHKbpIiJVteM8qQ"

def decrypt(data, key1, key2):
    ct = b64decode(data.encode("utf-8"))
    cipher2 = AES.new(key2, mode=AES.MODE_ECB)
    pt = cipher2.decrypt(ct)
    cipher1 = AES.new(key1, mode=AES.MODE_ECB)
    pt = cipher1.decrypt(pt)

    return pt

FLAG = decrypt(flag_en, b'wH1t3H@cK5_12252', b'wH1t3H@cK5_93658')

print(FLAG)
```

Then we ignore the rubbish at the back from the padding and collect our flag :)

```b'WH2022{M1dDl3_R0@d_15_tH3_b3sT_pLAc3_2_m33T}\x04\x04\x04\x04'```

### References

[1] https://en.wikipedia.org/wiki/Meet-in-the-middle_attack 
