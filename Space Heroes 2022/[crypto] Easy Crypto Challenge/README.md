# [crypto]  Easy Crypto Challenge  (356 pt)
Author: cdmann<br>
Difficulty: Hard

## Challenge description
My slingshotter cousin Maneo just discovered a new cryptography scheme and has been raving about it since. I was trying to tell him the importance of setting a **large, random private key**, but he wouldn't listen. Guess security isn't as important as how many thousands of credits he can win in his next race around the system.

I've recovered a message sent to him detailing the finish line. Can you decrypt the message to find the coordinates so I can beat him there? I'll give you a percentage of the score!

Enter flag as **shctf{x_y}**, where x & y are the coordinates of the decrypted point.

_Hint: You may wish to consult the great Sage of Crypto for help on this challenge._

### Files: 
* ecc.txt

---
## Solution
### TL;DR: Sage discrete_log to find private key
### Recon
* "large ... private key" - this means some sort of brute force might be involved :)
* ecc.txt - could this stand for more than "**E**asy **C**rypto **C**hallenge"? Lacking some experience, I did not immediately recognise it, but a quick google search told me that it also stands for Elliptic Curve Cryptography! :smile: [[1]](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) 
> For crypto, an elliptic curve is a plane curve over a finite field **m**. This mean it is a set of integer coordinates within the field (a square matrix of m*m), satisfying the equation **y^2 = x^3 + ax + b (mod m)** 
<br> And indeed, we note the equation matches the one in our txt file. 
* "the great Sage of Crypto" - naturally, we turn to SageMath [[2]](https://sagecell.sagemath.org/)

**Quick overview of ECC**
1. **Key Generation**: Maneo (Reciever) chooses a suitable curve `E(a,b)`, as well as a generator `G`. They also select an ideally "large, random private key" `d` for the encryption to be secure. The public key `P` is calculated with `P = d * G` --- (eq 1)
2. **Encryption**: 
* Maneo sends `E(a, b), m, G, P` to sender. 
* Sender chooses a random number `k` in (0, m-1), and calculates point `(x1, y1) = k * G` --- (eq 2) and `(x2, y2) = k * P`. <br>
    * _Note: If (x2, y2) happen to be the [point at infinity](https://en.wikipedia.org/wiki/Point_at_infinity), sender chooses another k and recalculates._ 
* Ciphertext `C = (x3, y3) + (x2, y2)` --- (eq 3) where `(x3, y3)` is the **message** (that we are trying to steal for the challenge)
* Finally, sender sends Maneo `C` and `(x1, y1)`
3. **Decryption**: Maneo/Reciever calculates `(x2, y2) = k * P = k * d * G = d * (x1, y1) --- (eq 4).` <br> Then `(x3, y3) = C - (x2, y2)`

For a deeper dive and better understanding, I found this pretty informative: https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc [3]

### Solving
Now, given that we appear to be missing the private key `d`, we need to solve the Discrete Logarithm Problem with `d` such that (eq 1) is satisfied. The challenge also tells us this key is unlikely to be "large" --> implying it must be small! (and thankfully, **Sage's discrete_log** function did work in our favour for this case). 

You can download SageMath, or use the online SageMathCell, as I have. <br><br>
_**sagemath**_
``` python
##INFO GIVEN & SET UP
a = 3820149076078175358
b = 1296618846080155687
m = 11648516937377897327  #modulus 
F = FiniteField(m) #points in elliptic curve are integers within field 
E = EllipticCurve(F,[a,b]) #setting up curve function 

G = E(4612592634107804164, 6359529245154327104) #generator 
P = E(9140537108692473465, 10130615023776320406) #public key 

x1y1 = E(7657281011886994152, 10408646581210897023) # (x1, y1) = k * G --- (eq 2)
C = E(5414448462522866853, 5822639685215517063) # C = (x3, y3) + (x2, y2) --- (eq 3)

##FINDING PRIVATE KEY d 
d = G.discrete_log(P) #such that P = d * G --- (eq 1)

##FINDING MESSAGE: (x3, y3)
x2y2 = d * x1y1 # (x2, y2) = k * P = k * d * G = d * (x1, y1) --- (eq 4)
x3y3 = C - x2y2 # --- (eq 3)
 
print("x3:" + str(x3y3[0]))
print("y3:" + str(x3y3[1]))
```
Output:
```
x3:8042846929834025144
y3:11238981380437369357
```

:triangular_flag_on_post: Hence, our flag is **shctf{8042846929834025144_11238981380437369357}**

### References

[1] https://en.wikipedia.org/wiki/Elliptic-curve_cryptography <br>
[2] https://sagecell.sagemath.org/ <br>
[3] https://cryptobook.nakov.com/asymmetric-key-ciphers/elliptic-curve-cryptography-ecc <br>

