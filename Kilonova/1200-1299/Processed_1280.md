Gigel is a great fan of mountain trips. At the same time, he is also a good computer scientist. He noticed that choosing a route between two tourist spots tires him less than choosing another route between the same spots. Gigel aims to find a model that allows him to determine a route on which, if he chooses, he will reach his destination as little tired as possible. Thus, he represents the terrain in which the two tourist spots are located through a two-dimensional array with $n$ rows (numbered from $1$ to $n$) and $m$ columns (numbered from $1$ to $m$), with elements strictly positive natural numbers, in which each element represents the altitude of a square-shaped terrain area with a side length of $1 \; m$. The effort to move from one area with altitude $c_1$ to a neighboring area with a higher altitude ($c_2$) is calculated as follows. A right triangle is drawn as in the figure:

~[excursie.png|align=right]

* $c_1$ and $c_2$ are the two altitudes, $c_1 < c_2$
* $1$ is the distance between the centers of the two neighboring areas
* $d = \sqrt{(c_2 - c_1)^2 + 1}$
* $\\alpha$ is the slope angle to be climbed

Then the effort is calculated as: $ef = d \cdot tg \ \alpha$.

In the following example, consider four neighboring areas with altitudes $1$, $2$, $6$, $10$. To get from the area with altitude $1$ to the area with altitude $10$, two routes can be chosen:

~[excursie-2.png|align=right]

1. directly, which involves an effort calculated as follows:
    - $ef = d \cdot tg \alpha = \sqrt{82} \cdot 9 \approx 81$.
2. indirectly, through the areas with altitudes $2$ and $6$, which involves an effort calculated as follows:
    - $ef = ef_1 + ef_2 + ef_3 = \sqrt{2} + \sqrt{17} \cdot  4 + \sqrt{17} \cdot  4 \approx 34$.

The effort to move from an area with altitude $c_1$ to a neighboring area with the same altitude is $1$. The effort to move from an area with altitude $c_1$ to a neighboring area with a lower altitude ($c_2$) is half the effort it would take to climb (i.e. from altitude $c_2$ to altitude $c_1$).

# Task

Write a program to determine the minimum effort to move from one tourist spot to another, with the path length not exceeding a given value $L_{max}$.

# Input data

The input file `excursie.in` contains:
- the first line contains two natural numbers $n$ and $m$ separated by a space, representing the dimensions of the terrain;
- the second line contains the real number $L_{max}$ representing the maximum allowable length of the path;
- the next $n$ lines each contain $m$ natural values, separated by space, representing in order the altitudes of the terrain areas;
- the last line contains four natural values $l_i$, $c_i$, $l_f$, $c_f$, separated by a space, where $l_i$, $c_i$ represent the row and column of the starting point, and $l_f$, $c_f$ represent the row and column of the destination point.

# Output data

The output file `excursie.out` will contain on the first line two real numbers separated by a space, $ef \; d$, representing the minimum effort required to move from one spot to another and the minimum length of a path traversed with minimum effort, respectively. The results will be displayed with three decimals.

# Constraints and clarifications

* $2 \leq n, m \leq 50$
* Moving from one area to another can be done in $4$ directions: ($N$, $E$, $S$, $W$). Specifically, if the current position is on line $i$, column $j$, by moving to $N$ the position changes to ($i-1, j$), to $E$ changes to ($i, j+1$), to $S$ changes to ($i+1, j$), and to $W$ changes to ($i, j-1$). (if these positions exist).
* Altitudes are natural numbers with values between $1$ and $100$.
* It is recommended to use $64$-bit real types. The result will be considered correct if the absolute difference between the displayed result and the correct result is < $0.01$
* $60\%$ of the score is awarded for correctly determining the minimum effort, and $100\%$ for correctly solving both requirements.

# Example

`excursie.in`
```
2 2
11
10 6
1 2
2 1 1 1
```

`excursie.out`
```
34.399 9.660
```

## Explanation

$\sqrt{2} +  8 \cdot \sqrt{17} = 34.399 (1.41421356+32.98484500=34.39905856)$
$\sqrt{2} +  2 \cdot \sqrt{17} =  9.660 (1.41421356+ 8.24621125= 9.66042481)$

The path is correct because the length of the road $9.660$ is less than the given value $L_{max} = 11$