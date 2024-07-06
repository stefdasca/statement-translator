~[image.png|align=right] 
Gigel received from his mother, as a homework, a sheet on which a series of $N$ integers was written. The only calculation he knew how to do until now was the sum of all the numbers. For this he placed $N-1$ addition signs, $+$, between the numbers located at consecutive positions in the series and thus calculated the sum of these numbers. Meanwhile, he grew up and also learned the multiplication operation for which he uses the sign $\\cdot$. From the series of $N-1$ addition signs, it occurred to him to replace $K$ plus signs with $K$ multiplication signs $\\cdot$.

He realizes that the homework is getting more complicated, as multiplications must be done before additions, but he does not give up and completes the calculation.

# Task

Write a program to determine the minimum value and the maximum value that can be obtained after the aforementioned replacement.

# Input data

The input file `optim.in` contains on the first line the natural numbers $N$ and $K$, separated by a space, representing the number of integers in the series, respectively the number of multiplication operations that will be performed. The second line contains $N$ integers separated by a space, $x_1, x_2, \\dots, x_N$, representing the numbers in the series.

# Output data

The output file `optim.out` will contain on a single line, separated by a space, in ascending order, the two required values.

# Constraints and clarifications

* $2 \\leq N \\leq 30$;
* $0 \\leq K \\leq 9; K \\lt N$
* $-8 \\leq x_i \\leq 8, 1 \\leq i \\leq N$
* If the output file contains exactly two numbers, but only one is correct, $40\\%$ of the score allocated to the respective test is obtained.

# Example

`optim.in`
```
6 3
2
0
3
-1
7
-4
```

`optim.out`
```
-31 86
```

## Explanation

$2 \\cdot 0 + 3 \\cdot (-1) + 7 \\cdot (-4) = -31$

$2 + 0 + 3 \\cdot (-1) \\cdot 7 \\cdot (-4) = 86$