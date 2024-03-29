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

We will work with these set of values for the solution:
```
[==!==] Bridged to timeline: 1a9f4
[==!==] Warning, controller corrupted, quantum core unstable. Match voltage immediately.
[==+==] System state:  _COEFFICIENT: 187.0198 (R/A), _PRECISION_RESISTOR: 523.55014 (R), _VOLTAGE: 47.2799 (V)
Please Enter _MODIFIABLE_RESISTOR resistance:
```
Let me define points Vc and Vd:

![image](https://user-images.githubusercontent.com/40383476/206493099-6b324704-8d0b-4c00-9777-1bb406d9f699.png)

Note that `_MODIFIABLE_RESISTOR` and `_CURRENT_RESISTOR` are parallel to `_UNKNOWN_RESISTOR` and `_PRECISION_RESISTOR`. A strategic first input would be 0Ω, because it allows us to derive potential at Vb. 

```
Please Enter _MODIFIABLE_RESISTOR resistance: 0
[==+==] Voltage across points: 19.3457 (V)
```

When `_MODIFIABLE_RESISTOR` = 0 Ω, <br>
Vd = Va = 47.2799 V <br>
Va - Vb = Vd - Vb = 19.3457 V <br>
=> Vb = 27.9342 V <br>

Let coefficient be C. <br>
V = RI, so Va - Vc = R<sub>_CURRENT_RESISTOR</sub> * I = C * I<sup>2</sup>  <br>

Also, Va - Vb = 0 => Va - Vc = Vb - Vc <br>
  (187.0198) * I<sup>2</sup> =  (27.9342 - 0) V  <br>
  I = 0.38648 A  <br>
  `_MODIFIABLE_RESISTOR` and `_CURRENT_RESISTOR` are connected in series, so same current I = 0.38648 A must flow through them.  <br>
  
Now, we want Va - Vb = 0, so Vd - Vb = Vd - Va = 19.3457 V   <br>
Then, potential difference across `_MODIFIABLE_RESISTOR` = Vd - Va = 19.3457 V  <br>
  19.3457 V = R<sub>_MODIFIABLE_RESISTOR</sub> * I =  R<sub>_MODIFIABLE_RESISTOR</sub> * 0.38648 <br>
  R<sub>_MODIFIABLE_RESISTOR</sub> = 50.056 Ω  <br>
  
```
[=!!!=] Warning quantum lock destablizing!
Please Enter _MODIFIABLE_REISTOR resistance: 50.056
[==+==] Voltage across points: 7.752375922365218e-05 (V)
[==!==] ...
[==0==] Quantum lock stablised. Beginning cleanup routines.
[=<0>=] STF22{L0ng_Qu8ntum_3hift}[=====] Shutting down..
```

🚩🚩🚩 ```STF22{L0ng_Qu8ntum_3hift}```
  
### Other thoughts 
Interestingly, we did not have to find `_UNKNOWN_RESISTOR` or even make use of the value given for `_PRECISION_RESISTOR`. Admittedly, I did not actually have the clarity of mind to come to the above solution right away, and spent some time calculating unecessary variables such as `_UNKNOWN_RESISTOR`. Using the potential divider rule, you would be able to find this: `_UNKNOWN_RESISTOR` = 523.55014 / 27.9342 * 19.3457 = 362.582
Having been told the set up is a "Wheatstone Bridge", we could make use of an online calculator to help find more values. <br>
<img width="412" alt="image" src="https://user-images.githubusercontent.com/40383476/206492675-cea81cd9-bb6a-4fa0-9c10-0a46905908a2.png">  
However, it results in more tedious calculations.
  
  
  
