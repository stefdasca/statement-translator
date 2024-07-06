After spending the night partying like a true student at the freshman ball, Armando arrives home at dawn and, after locking his door (like any responsible person), goes to sleep. He wakes up at dusk and realizes that he turned on several lights in the morning while struggling to get to bed. Unfortunately, Armando lives in a palace, so he has $N$ switches and $N$ bulbs (some on, some off). However, although he is rich, he couldn't find a skilled electrician, so, numbering the switches from left to right, switch $i$ changes its state and the state of all bulbs to its right. Formally, once switch $i$ is pressed, it changes the state of bulbs $i, i+1, i+2, \dots, N$. If a bulb was on, it turns off, and if it was off, it turns on.

# Task

Armando, still groggy from last night's party, asks for your help again. He asks you to tell him a way to turn off all the bulbs by pressing a **minimum** number of switches.

# Input data

The first line contains a natural number, $N$ (as described in the statement). The next line contains $N$ elements with values of $0$ or $1$. If the $i$-th element, from left to right, is $0$, then the $i$-th bulb is off. Similarly, if the $i$-th element is $1$, the bulb is on.

# Output data

The first line should contain the minimum number of switches Armando should press to turn off all the bulbs, and the second line should contain the indices of these switches, in the order they should be pressed. If there are multiple solutions with the minimum number of switch presses, any of them can be displayed.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$;
* At least one bulb is on;
* For 32 points, it is guaranteed that $1 \leq N \leq 1000$;
* For the remaining 68 points, there are no additional restrictions.

# Example

`stdin`
```
8
1 0 1 0 1 1 0 0
```

`stdout`
```
6
1 2 7 4 5 3
```

## Explanation

To turn off all the bulbs, he needs to press, in turn, switches $1$, $2$, $7$, $4$, $5$, and $3$. 
Before pressing any switch, the bulbs will look as follows:
~[lights_0.png]
After pressing switch $1$, the bulbs will look as follows:
~[lights_1.png]
After pressing switch $2$, the bulbs will look as follows:
~[lights_2.png]
After pressing switch $7$, the bulbs will look as follows:
~[lights_3.png]
After pressing switch $4$, the bulbs will look as follows:
~[lights_4.png]
After pressing switch $5$, the bulbs will look as follows:
~[lights_5.png]
After pressing switch $3$, the bulbs will look as follows:
~[lights_6.png]