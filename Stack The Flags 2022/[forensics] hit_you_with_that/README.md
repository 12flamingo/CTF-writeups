# [forensics] hit_you_with_that

## Challenge description
An adversary was observed to be exfiltrating a file from a music entertainment company that contains a to-be-released embargoed poster of a new song for one of their bands. Find the leaked file, which will contain the flag.

### Files:
* [STF22.pcapng](STF22_new.pcapng)
---
## Solution (in CTF)

**#0. Reflexive response: Look for files** </br>
I saw “file”… “poster”…. so I tried my luck with “Export Objects”… to no avail. 

<img width="300" alt="image" src="https://user-images.githubusercontent.com/40383476/206343432-92fa18ec-7fea-4413-af20-be08718a1c87.png">

If the poster had been sent via HTTP/FTP, we would have found it here.
(Occasionally, it saves you time in a CTF but not today, it seems.)

**#1. Sort by protocol** </br>
A quick glance through informs us that the pcap comprises many familiar protocols - all of which could potentially hold our flag. Personally I believe this is the main point we’re grappling with for the challenge - to systemically sort and eliminate irrelevant protocols. I speculated (based on past experience) that the flag/components of the flag would be isolated within each protocol. 

**#2. Zooming in to specific protocols** </br>
We are told to look for a “leaked file” so we will want to focus on protocols that can do such data transfer: 
* **TCP/HTTP**: I know there weren’t any objects in step 0, but maybe there are other clues (e.g. text/conversations) that could help? Hence, we follow the stream:
<img width= "600" alt="image" src="https://user-images.githubusercontent.com/40383476/206343400-8ca63c95-1aa8-4efb-a822-44bf4c2cf629.png">

Wow - a [youtube link](https://youtu.be/IHNzOHi8sJs?t=70) of blackpink. Unfortunately, no poster.
  
* **ICMP**: These packets look promising, because they are rather big (298 bytes) and there are quite a few. (Most of the time, if there’s nothing worth finding, I’d expect shorter packets - say, ~40-50 bytes)
We see some base64-esque data. Decrypting the very first ICMP packet, we get our flag! 
<img width="1316" alt="image" src="https://user-images.githubusercontent.com/40383476/206343783-d9cc4464-74c4-4c60-96e9-b890a739115f.png">

<img width="582" alt="image" src="https://user-images.githubusercontent.com/40383476/206343955-00173707-84fc-4edd-9318-0234fc0ea72b.png">

 🚩🚩🚩 ```STF22{Bl@ckPin9_V3n0m}```

Notice also that this is obviously a PNG header (PNG...IDHR...) - if we extract all the data from each of the ICMP packets, we would get our poster. However, there’s no time to waste in a CTF so that can wait until post-CTF. Here, we’ve found the flag but let’s just take a quick look at the last protocol to see why we would have realised the UDP packets are unhelpful.
* **UDP**:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/40383476/206344066-fda45b2b-c2fa-4dcb-80f9-75859bd784c9.png">

Looking at the data, each contains 300 bytes worth of “C”s. Indeed, nothing to see here.


## Post CTF
Out of curiosity, I wanted to see if I could get the poster. We recall that ICMP (ping) request and reply packets will contain the exact same data, so this means we should probably filter for only one of them. A closer look at the packet will make us see that only the packets with source 192.168.42.11 seem to have relevant data - the rest of the packets either repeat the same data (as a reply-request pair) or are empty.
  
<img width="1319" alt="image" src="https://user-images.githubusercontent.com/40383476/206344679-17c20360-877a-4701-ac7a-5eb2b650be9c.png">

_ip.src == 192.168.96.1 packets seem to contain Data:0000000... which is unhelpful_

Hence, we apply the filter "icmp and ip.src == 192.168.96.11". Here, tshark will come in helpful, allowing us to efficiently extract the data. 

```linux
tshark -r STF22.pcapng -Y "icmp and ip.src == 192.168.96.11" -T fields -e data | xxd -r -p | base64 --decode > blackpink.png
```

Let's break that down:
  * tshark flags: ```-r <input file> -Y <filter> -T fields -e <field>``` --> hexdump of data obtained, piped to...
  * ```xxd``` (-r: reverse hexdump to ASCII, -p: plain hexdump) --> ASCII, but base64 encoded, piped to...
  * ```base64 --decode``` --> stored in new png file
  
Thus, we obtain the [poster](blackpink.png), and running exiftool will also get us the same flag:
  
<img width="543" alt="image" src="https://user-images.githubusercontent.com/40383476/206345014-b40eb107-6a65-439e-8317-08e3bf374fd6.png">


