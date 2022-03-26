# [crypto] The Poem of Knowledge (767 pt/40 solves)
Author: xbowery<br>
Difficulty: Easy


## Challenge description
Our knowledgeable alien friend named Beale left us with a purported "_Poem of Knowledge_" before he went back to his universe.<br><br>He also dropped a message behind. Can you decipher what he was trying to say?<br><br>17-73-24-55-84-101-141-44-54-49-10-123-62-131-114-67-47-46-60-83-84<br><br>Note: Please wrap the flag with WH2022{...}<br>The flag is case-sensitive!"

### Files: 
* Poem of Knowledge.txt

---
## Solution
### TL;DR: Beale cipher - write a script… or use excel to solve

### Recon
My first response was to go down the rabbithole of performing a literary analysis on the Poem of Knowledge provided. I thought up all sorts of random (and eventually irrelevant) interpretations  - “two roads” could mean binary, and perhaps the one “not taken” to refer to a NOT operation? Or maybe the word “difference” means we ought to find the difference between the numbers.

Eventually though, after failing to produce a flag from binary and operations, I dejectedly returned to the challenge description - only to notice that the cipher’s identity had been fed to us all along! 

“**Beale**”, our alien friend, is a reference to the Beale cipher!

> To give you a quick idea, this cipher came about from this guy named Beale who hid some treasure in the 1800s and left 3 encrypted messages (a bunch of numbers) to his friend, before disappearing forever. His poor friend had no clue what to do and therefore it was eventually made public - and someone eventually solved the second one with the United States Declaration of Independence. (the key, or text needed to decrypt the numbers). [1] 

### Solving
To decrypt this substitution cipher, you essentially need a “key” (in this case our poem) as well as the chain of numbers. Now we **find the word corresponding to each number** (e.g. the first number is 17, and the 17th word is “I”. the second number is 73, and the 73rd word in the poem is "Had"), and we **take the first letter** of that word ("H"). Repeat for the rest of the numbers.

Great! We know what to do, and there are two ways to go about it:
1. Write a script 
2. Use an online tool

Being lazy, I went for option 2. Here are some tools you can find online:
* https://www.dcode.fr/book-cipher 
* https://www.braingle.com/brainteasers/codes/beale.php
<img width="952" alt="beale1" src="https://user-images.githubusercontent.com/40383476/160248876-dc3cfe16-b9f1-4d59-92ab-8a07ef58fb2c.png">_Image of Braingle Beale decrypt_

However, there was a problem: most if not all the tools disregarded the original capitalisation, but the flag was **case-sensitive**. The logical and perhaps more proper solution was clearly option one. But my reluctance to do any unnecessary thinking outweighed my pride and I decided to use excel to supplement the online tool :))))

**Step 1: Put one word in each cell** <br>
Data --> Text to columns 
<img width="1185" alt="beale2" src="https://user-images.githubusercontent.com/40383476/160248881-74371d30-67c7-4d55-8f71-0e5ca9491129.png">
**Step 2: Number each word** <br>
You get something like this: <img width="872" alt="beale3" src="https://user-images.githubusercontent.com/40383476/160248892-ea59ba8c-458c-4bf3-8aa9-d379ddb3d163.png"> <br>
**Step 3: Ctrl-F each number** to check for the **capitalisation** of each letter and modify the flag as necessary. <br>
Step 4: Profit (in pain)(and glee at the existence of excel for brainless solutions)

We end up with this:
```WH2022{IHopeYouhadagreattime}```

### References:

[1] https://en.wikipedia.org/wiki/Beale_ciphers

