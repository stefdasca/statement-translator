## Task

During the summer vacation, Phineas and Ferb want to build a roller-coaster. In the city of Danville, there are $N$ towers in a straight line. The $i$-th tower from left to right has the height $H_i$. A roller-coaster is formed from a subarray $R = \{i_1, i_2, \dots, i_k\}$ of the $N$ towers and the roller-coaster tracks that will be built between the pairs of towers $(i_1, i_2), (i_2, i_3), \dots, (i_{k-1}, i_k)$. It is well known that a track that connects a tower of height $A$ to a tower of height $B$ has a fun coefficient $gcd(A, B)$. The fun coefficient of a roller-coaster equals the sum of the coefficients of the tracks that make it up. Marcel promised to help Phineas and Ferb implement their plan in the hope of appearing in an episode. What is the maximum fun coefficient that can be obtained and for how many roller-coasters is it obtained?

## Input data

In the input file `rollercoaster.in` is $N$, the number of towers, and the second line contains the $N$ non-zero natural numbers.

## Output data

In the output file `rollercoaster.out` will contain 2 numbers, representing the maximum fun coefficient that can be obtained by Marcel, as well as the number of roller-coasters through which it is obtained modulo $1.000.000.007$.

## Constraints

$N \leq 250\ 000$ 

$H_i \leq 250\ 000$, 
$1 \leq i \leq N$

$i_1 < i_2 < \dots < i_k$

$gcd(A, B)$ is the greatest common divisor of $A$ and $B$

### Subtask 1 (20 points):

$N \leq 15$

### Subtask 2 (20 points):

$N \leq 1000$

### Subtask 3 (60 points):

initial constraints

The number of roller-coasters should be printed modulo $1.000.000.007$

## Example

`rollercoaster.in`

```
7
4 25 19 25 28 20 9
```

`rollercoaster.out`

```
32 2
```

## Explanation

We can take $R = \{1, 2, 4, 6, 7\}$ or $R = \{1, 2, 4, 5, 6, 7\}$.

Solution 1: If we choose $R = \{1, 2, 4, 6, 7\}$, the total fun coefficient will be: $gcd(H_1, H_2) + gcd(H_2, H_4) + gcd(H_4, H_6) + gcd(H_6, H_7) = 1 + 25 + 5 + 1 = 32$.

Solution 2: If we choose $R = \{1, 2, 4, 5, 6, 7\}$, the total fun coefficient will be: $gcd(H_1, H_2) + gcd(H_2, H_4) + gcd(H_4, H_5) + gcd(H_5, H_6) + gcd(H_6, H_7) = 1 + 25 + 1 + 4 + 1 = 32$.