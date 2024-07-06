# The Verone Millipede

The Verone millipede lives at most $12$ months, but this does not make it unhappy, as it finds life long and beautiful. It is called Verone because its cylindrical body is made up of colored segments, and each segment can only be one of the following colors: green, red, or black.

In the first month of its life, the millipede's body consists of a single segment. In each of the following months, each segment $s$ grows in length and divides into three segments: $s1, s2,$ and $s3$. Segments $s1$ and $s3$ keep the color of segment $s$, while the middle segment $s2$ colors itself as follows: if $s$ was green, then $s2$ becomes red. If $s$ was red, then $s2$ becomes black. If $s$ was black, then $s2$ becomes green.

Someone found a fragment of such a millipede, a result of a fatal fight with another creature.

# Task

Knowing the color of the unique segment in the first month of the millipede's life and the succession of colors of the found fragment, write a program that determines its age and the sequence of colors of all its segments before the fight began.

# Input data

The first line of the file `verone.in` contains a single character $c$, representing the color of the unique segment from which the millipede was formed in the first month of its life. The possible values for $c$ are `V`, `R`, or `N`. The second line contains a string of characters representing the colors of the segments of the found fragment. Each character in the string is one of the characters `V`, `R`, or `N`.

# Output data

The first line of the file `verone.out` will contain a natural number $v$, representing the age of the millipede at the time of the fight, expressed in calendar months. The second line will contain a sequence of characters representing the colors of all segments of the Verone millipede at the moment it was $v$ months old.

# Constraints and clarifications

* $2 \leq$ length of the fragment $\leq 40\ 000$;
* The characters on the second line of the input file are not separated by spaces;
* If there are multiple possible solutions, the one corresponding to the minimum age is considered;
* For determining the correct value of $v$, $40\\%$ of the total score is awarded.

# Example 1

`verone.in`
```
R
NR
```

`verone.out`
```
2
RNR
```

## Explanation

The millipede lost the fragment **NR** in the second month of its life. The colors of all its segments at that moment were: **RNR**.

# Example 2

`verone.in`
```
V
VRNRV
```

`verone.out`
```
3
VRVRNRVRV
```

## Explanation

The fragment **VRNRV** was lost in the third month. The colors of all segments of the millipede at that moment were: **VRVRNRVRV**.