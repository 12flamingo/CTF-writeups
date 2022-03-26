# [crypto] The Indecipherable Cipher
Author: WickedEye (Ying Keat)<br>
Difficulty: Easy

## Challenge description
Some say this cipher cannot be deciphered. Well, do you believe them?<br><br>Even worse, some say this cipher is misattributed!<br><br>I would say that the key to solving this challenge is to remember who the true inventor was

### Files:
* ciphertext.txt <br>
```CP2022{j1b3n3e3_15_Pcn_Xa3f@x_K1dC3R_0A_yB3F01Ys}```

---
## Solution
### TL;DR: Vigenère cipher, key: Giovan
### Recon
Challenge description says it all in two very helpful phrases:
1. “cipher is misattributed!” - a quick google search will inform us that it is likely the **Vigenère cipher**
![crypto_indec1](https://user-images.githubusercontent.com/40383476/160249386-1ea484d5-ed02-4f19-a2e0-d9621d92f622.png)
3. “key … is … the true inventor”  - we even have the key! (sort of)
Let’s do a bit of reading:
![crypto_indec2](https://user-images.githubusercontent.com/40383476/160249387-4f8bd061-0ee2-48b9-b298-21956a4bb11c.png)

### Solving 
Pleased with the findings, I put what I thought was the “key” (Giovan Battista Bellaso) into dcode (https://www.dcode.fr/vigenere-cipher) and received 
```WH2022{v1g3n3r3_15_Ocu_Es3n@e_K1cY3G_0P_yJ3R01Sk}```
as output. Alas, I was Wrong - because I was too impatient to read the entire flag :c

Upon a closer look, the only intelligible word in that sequence is “vigenere”. After several minutes of disbelief, opening a ticket just to be sure (sorry chall admins!), and trying other online tools, I finally came to my senses and realised the key was only the first name (**Giovan**). (because the first part was right while the latter half was obviously rubbish)

After I found out we’re on first-name basis with Giovan, I had no problem extracting the actual flag!
```WH2022{v1g3n3r3_15_Juz_Ca3s@r_C1pH3R_0N_sT3R01Ds}```
