## Sequences

Danut has a mischievous computer. To be able to use it, he has to answer a question every morning. Today, when he woke up, Danut saw two sequences of numbers on the computer monitor, each containing $N$, respectively $M$ numbers. Let’s denote the first sequence by $x_1, x_2, \dots, x_N$, and the second sequence by $y_1, y_2, \dots, y_M$. The computer asks him to find three numbers $k$, $p$, and $q$ such that $x_p + y_q = x_{p+1} + y_{q+1} = \dots = x_{p+k-1} + y_{q+k-1}$. If there are multiple such triplets, Danut must choose the one with the maximum $k$. If there are multiple triplets with the maximum $k$, he can answer with any of them.

## Task

Determine $k$, $p$, and $q$ such that the above conditions are met.

## Input data

The first line of the file `siruri.in` contains a number $N$ representing the number of elements in sequence $X$. The second line of the file contains $N$ numbers: $x_1, x_2, \dots, x_N$. The third line contains the number $M$ representing the number of elements in sequence $Y$. The fourth line contains $M$ numbers: $y_1, y_2, \dots, y_M$.

## Output data

The output file `siruri.out` will contain the numbers $k$, $p$, and $q$.

## Constraints and clarifications
1 $\leq$ $N$, $M$ $\leq$ 100\ 000 

-100\ 000 $\leq$ $X_i$ $\leq$ 100\ 000, for 1 $\leq$ $i$ $\leq$ $N$ 

-100\ 000 $\leq$ $Y_j$ $\leq$ 100\ 000, for 1 $\leq$ $j$ $\leq$ $M$

$k$ can be 1 

## Example

siruri.in 

`8 -100 -100 -100 1 2 3 4 5 6 5 4 3 2 1`

siruri.out 

`5 4 1`

## Explanation

5+1 = 4+2 = 3+3 = 2+4 = 1+5.