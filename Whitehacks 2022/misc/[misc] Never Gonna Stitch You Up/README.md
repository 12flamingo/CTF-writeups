# [misc] Never Gonna Stitch You Up (233 pt/65 solves)
Author: xbowery <br>
Difficulty: Easy

## Challenge description
We have received a file from the aliens, but it got malformed halfway during transmission. Can you retrieve the flag from this file?

### Files:
* get_rickrolled.mp4
---
## Solution
### TL;DR: strings
### Recon
Reading “malformed halfway during transmission”, I initially thought we’d have to do a corrupt file repair! 
### Solving 
Acting on my suspicions, I opened it up in HexEd.it. I then took a look at the start and end of the file because that’s where you usually find things that aren’t quite right. The start looked pretty good - the file signature was intact. But scrolling to the bottom we see something suspicious: 

<img width="599" alt="misc_never1" src="https://user-images.githubusercontent.com/40383476/160250101-ba61b0cf-9447-4cb3-aeb7-6e88f805453a.png"> 

Of course, you could find the flag in the hexeditor too. But it is much easier to run ```strings get_rickrolled.mp4``` which will help you see it with much less suffering. 

<img width="349" alt="misc_never2" src="https://user-images.githubusercontent.com/40383476/160250117-8c4ead31-5cc4-497f-9ce2-55b179474b48.png">

```WH2022{5tr1ng_m3_up_b3f0r3_y0u_g0_go}```
