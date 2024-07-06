In one day, Ioana wrote all natural numbers of $N$ digits each, simultaneously fulfilling the conditions:
* The number formed by the first two digits is a perfect square;
* The third digit is necessarily a prime number;
* It does not contain two adjacent even digits nor two adjacent odd digits.

For example, the three-digit numbers written by Ioana are: $163$, $165$, $167$, $252$, $363$, $365$, $367$, $492$, $812$.

# Task

Given the numbers $N$ and $X$, write a program that determines:
1. how many numbers of $N$ digits meet the three conditions from the statement;
2. what is the closest number to $X$, different from $X$, that fulfills the three conditions from the statement and has the same number of digits as $X$. If there are two such numbers, equidistant from $X$, the smaller one will be displayed.

# Input data

The input file `numere.in` contains on the first line a natural number $C$. The number $C$ can only have values $1$ or $2$. The second line contains, in the case of the first task, the number $N$, and in the case of the second task, the number $X$.

# Output data

If the value of $C$ is $1$, only the first task will be solved. In this case, the output file `numere.out` will contain on the first line a natural number representing the result determined for the first task.

If the value of $C$ is $2$, only the second task will be solved. In this case, the output file `numere.out` will contain on the first line a natural number representing the result determined for the second task.

# Constraints and clarifications

* $3 \leq N \leq 29$;
* $100 \leq X \leq 20 \ 000 \ 000$;
* For solving the first task, $30$ points are awarded, and for solving the second task, $70$ points are awarded.

# Example 1

`numere.in`
```
1
4
```

`numere.out`
```
45
```

## Explanation

The four-digit numbers written by Ioana are: 1630, 1632, 1634, 1636, 1638, 1650, 1652, 1654, 1656, 1658, 1670, 1672, 1674, 1676, 1678, 2521, 2523, 2525, 2527, 2529, 3630, 3632, 3634, 3636, 3638, 3650, 3652, 3654, 3656, 3658, 3670, 3672, 3674, 3676, 3678, 4921, 4923, 4925, 4927, 4929, 8121, 8123, 8125, 8127, 8129.

# Example 2

`numere.in`
```
2
200
```

`numere.out`
```
167
```

## Explanation

The closest number to $200$ is $167$ (the three-digit numbers written by Ioana are: $163$, $165$, $167$, $252$, $363$, $365$, $367$, $492$, $812$).