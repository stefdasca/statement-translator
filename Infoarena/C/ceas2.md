## Task

Gigel has recently moved to the planet Gigelonia. Among the myriad of fascinating things he found in his new adventure on this planet, Gigel was most fascinated by the clocks. Unlike earthly clocks, these clocks display the current hour and minute using a string of $N$ small letters of the English alphabet. Staring for hours at this fascinating clock, Gigel began to imagine how it would be if he could change time at will using the following operation: Choose 2 letters $c_{1}$ and $c_{2}$. All occurrences of the letter $c_{1}$ in the code will be swapped with the letter $c_{2}$. Being passionate about computer science, Gigel wants to build a program that tells him whether he can travel in time using this operation. Given the code of the current time and the code of the time Gigel wants to travel to, help him discover the answer! If he can travel in time, Gigel also asks you to specify the operations necessary for this.

## Input data

The input file `ceas2.in` will contain on the first line the current time code, followed by the second line containing the time code in which Gigel wants to travel.

## Output data

The output file `ceas2.out` will contain on the first line the answer to the question: YES - if Gigel can travel to the desired time, NO - if Gigel cannot travel to the desired time. If the answer is YES, each of the following lines of the output file will contain two characters, $c_{1}$ and $c_{2}$, representing the operations necessary for time travel. These operations will be printed in lexicographical order.

## Constraints and clarifications

1 $\leq$ $N$ $\leq$ 100000 

The number of operations performed should be minimal!

## Example

`ceas2.in`
```
abebbfdcu
akekkfpcx
```

`ceas2.out`
```
YES
b k
d p
u x
```