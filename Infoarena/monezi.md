# Coins

Prince Algorel has $N$ types of gold coins in the castle treasury. For each type, the value of the coins of that type is known. The prince's wealth is immense, so it can be considered that he has an infinite number of coins of each type. To free the princess from the hands of the greedy baron, he does not need to perform an act of bravery; he just has to give the baron coins with a total value of $S$. Although he wants to see the princess as soon as possible, Algorel starts to think about all sorts of problems related to his treasury. For example, he defines for a subset of coin types, let's call it $X$, the coverage capacity of this subset as the number of sums between $1$ and $S$ (inclusive) that he can obtain using only coins of the types in subset $X$. From this thought to calculating the sum of the coverage capacities of all possible subsets of coins was only a step.

## Task

Calculate for Algorel the sum of the coverage capacities of all subsets of coin types in his treasury (in total there are $2^N - 1$ possible sets). Only after finding the answer to this problem can Algorel focus on freeing the princess.

## Input data

The first line of the file `monezi.in` contains two integers separated by a space, $N$ and $S$, representing the number of coin types and the sum that needs to be paid to the baron. The next $N$ lines contain one integer each, $V[i]$, representing the value of a coin of type $i$.

## Output data

The output file `monezi.out` will contain the number that Algorel wants to find, representing the sum of the coverage capacities of all subsets of coins in his treasury.

## Constraints and clarifications

$1 \leq N \leq 17$

$1 \leq S \leq 512$

The values of the coins will be natural numbers between $1$ and $500$

No two types of coins will have the same value

Multiple coins of the same type can be used

For $50\%$ of the tests $N \leq 10$

## Example

`monezi.in`

```
2 10
2
3
```

`monezi.out`

```
17
```

## Explanation

With the subset $\{2\}$, 5 sums can be obtained: $2, 4, 6, 8, 10$

With the subset $\{3\}$, 3 sums can be obtained: $3, 6, 9$

With the subset $\{2,3\}$, 9 sums can be obtained: $2, 3, 4, 5, 6, 7, 8, 9, 10$

Note that it is not mandatory to use all types of coins in a subset: for example, the sum $6$ for the last subset is obtained using only type $2$ coins or only type $3$ coins (if we use both, we cannot obtain the sum $6$). The number sought by Algorel will thus be $5+3+9=17$.