# [crypto] Wow! (100 pt)
Difficulty: Easy

## Challenge description
Jerry R. Ehman is frequently observing incoming signals from OSU's big ear radio telescope again when he stumbled across another interesting signal! This time the signal was followed by a mysterious png. What does it all mean?

### Files: 
* signal.png
* woah.png

---
## Solution
### TL;DR: Manual.. frequency.. analysis...
I am writing this mostly for the fun of it, and the silliness of what I did to get the flag. 
### Recon
I had no idea what "Wow!" or the "signal" was referencing. But of course, Google and Wikipedia are here to save the day! [1] 
> The Wow! signal was a strong narrowband radio signal detected on August 15, 1977, by the Ohio State University's Big Ear radio telescope in the United States, then used to support the search for **extraterrestrial intelligence.** Astronomer Jerry R. Ehman discovered the anomaly a few days later while reviewing the recorded data. He was so impressed by the result that he circled on the computer printout the reading of the signal's intensity, "6EQUJ5", and **wrote the comment "Wow!"** beside it
![Wiki image](https://user-images.githubusercontent.com/40383476/161581534-a6e42139-4ef7-49ab-a260-426e184f9d90.png)

That looks an awful lot like the one this challenge gave us: (Disclaimer, I never used it in the end 😔)
![signal.PNG](https://user-images.githubusercontent.com/40383476/161581825-282cb930-19b3-4515-888e-7a27dcda9c0f.png)

### Solving
After going around in a few more circles, I was still no closer to deciphering the mysterious annotations on the signal.png.  Alright, so what DID I do? 
![woah.png](https://user-images.githubusercontent.com/40383476/161583861-ae0d3f47-5611-46c7-b430-6224d070b49f.png)
**[RED] Stage 1:** My eyes were drawn to the _ _ _ _ _ {XXXXXXX} format that was almost cetainly our flag. Hence, I could identify the first 5 characters as "shctf" and map the repeated characters inside the flag from the wrapper - I use uppercase letters to annotate the "confirmed" letters and lowercase for the ones I guessed in the following stages:

**[GREEN] Stage 2: **I decided that _ TS and TH _ was fairly likely to be 'its' and 'the' - how many other english words followed that structure? Not many. There is also an 'i' symbol in the last word. 

**[BLUE] Stage 3:** Now, there was nothing else I could decipher from that line alone. Skimming the passage, we notice many isolated spiral characters. The only one-letter words in English are a and I (see circled chars) - and we've already used 'i' in the above stage. Hence, I substituted 'a' into the spiral characters from the flag. 

**[ORANGE] Stage 4:** Here's where the context comes in useful. As I kept the phrase "extraterrestrial intelligence" at the back of my mind, I predicted that the last word would be "martians"! 

**Stage 5:** So... what was the three-lettered, palindromic first word I had yet to uncover? I was stumped for a good moment before I remembered the title: wow

Piecing together my intelligent guesses, it looked like a passable flag:

🚩 `shctf{wow_its_the_martians}`

### Additional notes/thoughts
I'm definitely not very proud of how I scraped through this challenge with a very guess-esque technique. But in hindsight, I found it a little funny. Desperation can induce creativity, I suppose. I await the intended solution :')

### References 
[1] https://en.wikipedia.org/wiki/Wow!_signal
