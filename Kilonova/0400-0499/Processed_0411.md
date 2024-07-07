Legend has it that, a long time ago, in the city of Suceava, a treasure of infinite value was buried. Fascinated by this theory, you decided to try your luck as well.

Fortunately, amateur archaeologists on social media have proposed a list of `N` popular locations for treasure burial, all placed in a line along the plains of Suceava. Furthermore, you have found on the internet a professional treasure detecting app whose radar claims to have an infinite detection power and in which you can even set the desired treasure to be found!

The problem is that this application consumes the phone’s battery, and you wish to be economical, so you decided not to keep the phone on continuously, but to turn it on only in different possible locations. Thus, you can choose to go to a location and turn it on. The app will tell you if the treasure is in that place, or otherwise, it will show you the direction to it. This direction can be to the right or left, depending on the true location of the treasure.

Unfortunately, due to electrostatic discharges in the air, depending on where you decide to detect the treasure, the app may require more calibration time, thus consuming more battery. Specifically, to turn on the detector at location `i`, you will consume $C_i$ units of battery. You do not know where the treasure is buried, so you want to make sure the phone will not run out of battery without finding the treasure, wherever it may be buried.

# Task
Given the number of battery units consumed for each of the `N` locations, what is the minimum number of battery units you will need to ensure you will find the treasure using the detector, wherever it may be, before the phone runs out of battery?

# Input data
The first line of the input file `takara.in` contains a positive integer `N`, representing the number of possible locations. The second line contains `N` positive integers $C_i$, separated by spaces, as described above.

# Output data
The first line of the output file `takara.out` will contain a single positive integer, representing the minimum number of battery units needed to find the treasure, wherever it may be.

# Constraints and clarifications
* `1 \\leq N \\leq 5\ 000`
* $1 \\leq C_i \\leq 200\ 000$
* For tests worth `15` points, `1 \\leq N \\leq 500`
* For other tests worth `55` points, `1 \\leq N \\leq 2\ 000`

# Examples
`takara.in`
```
4
10 1 5 2
```
`takara.out`
```
3
```

Explanation
---
You start by checking location `2`, consuming one battery unit.
If the app directs you to the left, you will know that the treasure is at location `1`.
If it directs you to the right, you will check location `4`, consuming another two units.
After this, you will know for sure where the treasure is.

`takara.in`
```
6
73 33 44 25 6 70
```
`takara.out`
```
58
```

`takara.in`
```
9
91 35 21 55 30 45 53 29 91
```
`takara.out`
```
96
```

`takara.in`
```
20
18 32 37 17 22 13 3 35 20 30 37 32 10 23 9 5 27 36 27 22
```
`takara.out`
```
65
