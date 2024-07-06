In the midst of the preparations for the Normandy landing (from the Second World War), the German counterintelligence officers observed that all sorts of individuals started to pass through the border points, with letters and digits engraved on their belts. After they managed to catch some of them and confiscated their belts, they found that there were always a number $n$ of letters and digits on the belt. After prolonged "interviews," they found out that the belts encoded the lines and modes of attack in numerical form, in base $16$.

To decode the message, the belt was cut into $\sqrt{n}$ pieces which were then placed one below the other, and the characters on each column were read from top to bottom, while the number formed on a column was transformed into base $10$. If the resulting number had digits in strictly increasing order, the infantry would attack first, if it was strictly decreasing the aviation would attack first, otherwise, the attack would be combined (mixed). The number of attack lines is equal to $\sqrt{n}$.

# Task

Write a program that, reading the information from a belt, determines the number $x$ of attack lines and the mode in which the attack will occur.

# Input data

The first line of the file `debarcare.in` contains the message. The letters in the message will be only uppercase letters.

# Output data

The first line of the file `debarcare.out` will contain the number $x$, and on the following $x$ lines, one of the words infantry, aviation, mixed depending on the type of attack.

# Constraints and clarifications

* $n$ is a perfect square, strictly less than $100$
* The numbers formed in base $10$ have at least two digits.
* The possible letters are $A$, $B$, $C$, $D$, $E$, $F$

# Example 1

`debarcare.in`
```
01C7A8BAA
```

`debarcare.out`
```
3
infantry
mixed
aviation
```

## Explanation

If we cut the belt and place the pieces one below the other, we get:
```
01C
7A8
BAA
```

Thus, the numbers in base $16$ will be: $07B$, $1AA$, $C8A$, whose values in base $10$ will be: $123$, $426$, $3210$.