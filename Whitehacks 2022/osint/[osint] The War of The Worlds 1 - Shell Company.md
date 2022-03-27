# [osint] The War of The Worlds 1 - Shell Company (957 pt/20 solves)
Author: Hartanto<br>
Difficulty: Easy

## Challenge description
Anyway, before Lewis disappeared, he got alerted that some company is providing CTFSolver-as-a-Service. I mean, what kind of cruel human being would take away all the F(un) from CTF, and we surely don't want anyone to be using their service for our upcoming CTF.<br><br>
Check this out: https://github.com/CTFSolverService<br><br>In any case, find out who owns the company. Maybe they have something to do with Lewis's disappearance.<br><br>Flag is in the format: WH2022{FullNameWithNoSpaceAndInitialCaps}

---
## Solution
### Recon
<img width="982" alt="pgp1" src="https://user-images.githubusercontent.com/40383476/160249592-67caea75-ac9d-4236-8e75-9391a3ef9b7c.png">
Have to say, this one stumped me for a fair bit of time. What on earth could we use the key for? It certainly wasn’t any good for SSH or github itself. 

### Solving
Let’s consider: how do you typically contact someone?
1. Social media: Nope, no twitter, instagram, facebook, reddit in sight for our solver service owner
2. Phone number: That… does not resemble a phone number
3. Email: Well, it doesn’t resemble an email either.

However, throwing around random search terms on Google like “16 character/digit key”, “email”, “phone”, “reverse lookup” did me some good because they led me to discover that **PGP KeyIDs** resembled this mysterious string! 

Afterwards, it was a much simpler matter of doing a reverse lookup for the keyID on https://pgp.mit.edu/ 
<img width="751" alt="pgp2" src="https://user-images.githubusercontent.com/40383476/160249593-8939989e-8ce8-4d00-9f81-924024a02185.png">

```WH2022{NgEnSiangKurt}```
