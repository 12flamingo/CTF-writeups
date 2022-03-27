# [forensics] Hidden_in_plain_sight (1000 pt/2 solves) -- <br> solved post-CTF
Author: Louis (L0j0)
<br>Difficulty: Easy-Medium

## Challenge description
Planet X0507-LJL has decided to run the inaugural galactic exchange program with the students from their planet with our Earth. While gathering images of the different universities on Earth, Planet X0507-LJL discovered an image containing hidden information amongst the images of the different universities. The information seems to be hidden in the bits. Help them crack this image and figure out the hidden transmission! 

### Files:
* SMU_hidden.png
---
## Solution
### Recon
"hidden in the bits" implies that it is some from of **LSB (least significiant byte) steganography**. This makes us think of **zsteg**. 

### Solving 
My initial hunch turned out right because running zsteg yields a suspiscious looking string in b1,bgr,lsb,xy:

```bash command-line
zsteg SMU_hidden.png 
imagedata           .. text: "\r\r#0329?\n"
b1,r,msb,xy         .. text: "dUnae A6"
b1,rgb,lsb,xy       .. text: "s,A.ZPR\\"
b1,bgr,lsb,xy       .. text: "QH4sICMzDCWIAA2ZsYWcudHh0AAv3MDIwMqoON85JNshNjS8xiA/2DY13Mi4uiQ/NM6wFAMovwkIfAAAA\n" 
b2,r,lsb,xy         .. text: "@\n~.QOdI:@J"
b2,r,msb,xy         .. file: Novell LANalyzer capture file
b2,g,lsb,xy         .. text: "`S\t1&\"*W&"
b3,b,msb,xy         .. file: OpenPGP Public Key
b3,rgb,lsb,xy       .. file: zlib compressed data
b3,bgr,msb,xy       .. file: OpenPGP Public Key
b4,r,lsb,xy         .. text: "BVRHbTC\"#4UV"
b4,r,msb,xy         .. file: StarOffice Gallery theme  DQ??Ԙ?dE?n?C??B, 168559359 objects, 1st ??	

b4,g,lsb,xy         .. text: "\"233434Vxgwfg"
b4,b,msb,xy         .. text: "]UUUUUUUUUUUU"
```

Although my eyes were drawn to ``` QH4sICMzDCWIAA2ZsYWcudHh0AAv3MDIwMqoON85JNshNjS8xiA/2DY13Mi4uiQ/NM6wFAMovwkIfAAAA```, here's when things went wrong. Unfortunately, base64 decoding what looked like a very promising string produced rubbish: <br>
```
@~, #3%�
�/ʨ89$!64 ?65ȸ$?4ΰ(	|��
```
This seemingly dead-end inspired me to veer completely off-track and try a multitude of irrelevant strategies, from extracting the other datastreams into files that obviously did not lead anywhere, to attempting to locate the original source image and comparing it to the modified file. Worse still, the more time and hope I invested into this challenge, the more I fell into the sunk cost fallacy and wasted a precious hour or perhaps more. 

### Post-CTF continuation
I was later redirected back to the initial track of action (with zsteg and base64), after being told you had to remove the leading 'Q'. In hindsight, I realise one might have recognise the telling "H4sI" that hints at a gzip. 

In any case, base64 decoding with 
``` echo H4sICMzDCWIAA2ZsYWcudHh0AAv3MDIwMqoON85JNshNjS8xiA/2DY13Mi4uiQ/NM6wFAMovwkIfAAAA | base64 --decode```
yields
```??	bflag.txt```. This makes us think to do a hexdump so we can identify what is going on. 
```
1f8b0808ccc309620003666c61672e747874000bf730323032aa0e37ce4936c84d8d2f31880ff60d8d77322e2e890fcd33ac0500ca2fc2421f000000
```

We should now recognise the file signature of a GZIP archive file. ```1f8b08```
Unzipping with https://codebeautify.org/gzip-decompress-online, we obatin the flag.

```WH2022{W3lc0me_t0_SMU_B3st_Un1}```



