# [hardware] Quantum Watch

## Challenge description
Jaga was tasked to investigate a disturbance in a local village, and after some sleuthing, found an abandoned research facility on the outskirts of the village. An initial search of the place led them to the central research room where it looked like a large disturbance had occured: everything was wildly scattered across the lab with upturned tables, sparking equipment and various bits of research documents scattered everywhere.

In the center of the mess was a watch that looked nothing like Jaga had seen before. It was perfectly symmetrical, and the shadows seemed to fade directly into darkness without hint of an edge.

Jaga, curious, put the watch on, and it instantly locked onto their wrist! An error message began to print out on the screen, and a heartbeat later, the research lab seemed to warp around Jaga. When Jaga tried to escape from the lab to seek help, they were reset back to the moment where the watch started to lock.

Help Jaga to fix the watch and escape the time loop!

### Files:
* [schematics.png](schematics.png)
---
## Solution 
I've written here the most straightforward and mathematically leisurely approach that comes to mind. However before we get into it, let's examine the problem.

![image](https://user-images.githubusercontent.com/40383476/206436706-dc692c87-3a2a-4bb8-bdef-7b4c8bf316a3.png)

Here's what a typical input/output exchange would look like after we connect to the service:
```
[==!==] Bridged to timeline: d726d
[==!==] Warning, controller corrupted, quantum core unstable. Match voltage immediately.
[==+==] System state:  _COEFFICIENT: 182.3486 (R/A), _PRECISION_RESISTOR: 1138.08096 (R), _VOLTAGE: 70.1121 (V)
Please Enter _MODIFIABLE_RESISTOR resistance: 0
[==+==] Voltage across points: 20.8737 (V)
[=!!!=] Warning quantum lock destablizing!
Please Enter _MODIFIABLE_REISTOR resistance: 0  
[==+==] Voltage across points: 20.873728341454104 (V)
[!!!!!] Quantum core failure detected!
[=!!!=] Engaging failsafes. Stepping left...
[=====] Stable timeline c4857 found, generating bridge...
[==!==] Local flux corruption > 99.1%. Unable to jump further back than 0.02s
```
I first set the modifiable resistor as 0Ω for both inputs with significant time lag between my inputs, to check if the rest of the resistors and hence the volatage across points would change with respect to my first input: It did not. (Voltage across points remains the same). This hints that keying in a strategic first input will probably help us derive additional information that will determine the correct value for `_MODIFIABLE_RESISTOR` which we can input the second time we are asked. 

**Aim: Input a `_MODIFIABLE_RESISTOR` value that will give output of `Voltage across points` = 0V**



### Other thoughts 
I did not actually have the clarity of mind to come to the above solution right away, and actually spent some time calculating unecessary variables such as `_UNKNOWN_RESISTOR`. For the sake of doe
